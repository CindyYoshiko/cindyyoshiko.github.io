#!/usr/local/bin/perl
use Jcode;

# Copyright (C) 2001-2003 All right reserved by Shinya Kondo ( CGI KON )

	require "cgi-lib.pl";

	&ReadParse;

sub err_input{
print "Content-type: text/html\n\n";
print qq!
<HTML>
<HEAD>
	<TITLE>�øŵ����������Ŵ����ˤ��񻲲ÿ�������</TITLE>
	<META Http-Equiv="Content-Type" Content="text/html;charset=EUC-JP">
</HEAD>
<BODY>
<CENTER>
<TABLE BORDER="0" BGCOLOR="#EEEEEE" CELLPADDING="20" WIDTH="60%">
	<TR>
		<TD ALIGN="center">
			<FONT SIZE="4"><B>�øŵ����������Ŵ����ˤ��񻲲ÿ�������</B></FONT>
		</TD>
	</TR>
	<TR>
		<TD ALIGN="center">
			<P>
			<FONT COLOR="#FF0000">���Ϲ��ܤ��Դ����Ǥ�</FONT>
		</TD>
	</TR>
</TABLE>
</CENTER>
</BODY>
</HTML>
!;
}

# �ᥤ��ץ����

	if($in{'send'}) {
	    unless ($in{'name'} && $in{'kana'} && $in{'add1'}&& $in{'add2'}){
		err_input;
                exit;
            };

		my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
		$year += 1900;
		$mon += 1;

		if(open(OFILE,">>/home/cindy/kako.csv")) {
			$in{'note'} =~ s/\x0D\x0A|\x0D|\x0A/<BR>/g;

			$record .= $in{'name'}.",";
			$record .= $in{'kana'}.",";
			$record .= $in{'postal'}.",";
			$record .= $in{'add1'}.",";
			$record .= $in{'add2'}.",";
			$record .= $in{'tels'}.",";
			$record .= $in{'mail'}.",";
			$record .= $in{'note'}.",";
			$record .= sprintf("%04dǯ%02d��%02d��,",$year,$mon,$mday);
			$record .= sprintf("%02d��%02dʬ%02d��\n",$hour,$min,$sec);
			print OFILE jcode($record)->sjis;
			close(OFILE);
			$info = "��������λ���ޤ�����";
		} else {
			$error = "�����Ǥ��ޤ���Ǥ�����";
		}

		require "member_1.tmpl";
		exit;
	}

# �����Ͽ�ե������ɽ��

print "Content-type: text/html\n\n";
print qq!
<HTML>
<HEAD>
	<TITLE>�øŵ����������Ŵ����ˤ��񻲲ÿ�������</TITLE>
	<META Http-Equiv="Content-Type" Content="text/html;charset=EUC-JP">
</HEAD>
<BODY>
<FORM ACTION="kako.cgi" METHOD="post">
<CENTER>
<TABLE BORDER="0" BGCOLOR="#EEEEEE" CELLPADDING="10">
	<TR>
		<TD ALIGN="center">
			<FONT SIZE="4"><B>�øŵ����������Ŵ����ˤ��񻲲ÿ�������</B></FONT>
			<P>
			<FONT SIZE="2">�� �ʲ��ι��ܤ����Ϥ�������������פ򥯥�å����Ʋ�������</FONT><BR>
			<FONT COLOR="#FF0000"></FONT><BR>
			<TABLE BORDER="0" CELLPADDING="3">
				<TR>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">��˧̾</FONT></TD>
					<TD><INPUT TYPE="text" NAME="name" SIZE="30"></TD>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">�եꥬ��</FONT></TD>
					<TD><INPUT TYPE="text" NAME="kana" SIZE="30"></TD>
				</TR>
<TR>
<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">͹���ֹ�</FONT></TD>
					<TD><INPUT TYPE="text" NAME="postal" SIZE="9"></TD>
</TR>
				<TR>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">�潻��</FONT></TD>
					<TD COLSPAN="3">
						<SELECT NAME="add1">
							<OPTION>�̳�ƻ
							<OPTION>�Ŀ���
							<OPTION>��긩
							<OPTION>�ܾ븩
							<OPTION>���ĸ�
							<OPTION>������
							<OPTION>ʡ�縩
							<OPTION>��븩
							<OPTION>���ڸ�
							<OPTION>���ϸ�
							<OPTION>��̸�
							<OPTION>���ո�
							<OPTION selected="selected">�����
							<OPTION>�����
							<OPTION>������
							<OPTION>Ĺ�
							<OPTION>���㸩
							<OPTION>�ٻ���
							<OPTION>���
							<OPTION>ʡ�温
							<OPTION>���츩
							<OPTION>�Ų���
							<OPTION>���θ�
							<OPTION>���Ÿ�
							<OPTION>���츩
							<OPTION>������
							<OPTION>�����
							<OPTION>ʼ�˸�
							<OPTION>���ɸ�
							<OPTION>�²λ���
							<OPTION>Ļ�踩
							<OPTION>�纬��
							<OPTION>������
							<OPTION>���縩
							<OPTION>������
							<OPTION>���縩
							<OPTION>���
							<OPTION>��ɲ��
							<OPTION>���θ�
							<OPTION>ʡ����
							<OPTION>���츩
							<OPTION>Ĺ�긩
							<OPTION>���ܸ�
							<OPTION>��ʬ��
							<OPTION>�ܺ긩
							<OPTION>�����縩
							<OPTION>���츩
						</SELECT>
					<INPUT TYPE="text" NAME="add2" SIZE="58">
					</TD>
				</TR>
				<TR>
					<TD NOWRAP><FONT SIZE="2">�������ֹ�</FONT></TD>
					<TD><INPUT TYPE="text" NAME="tels" SIZE="30"></TD>
					<TD NOWRAP><FONT SIZE="2">E-mail</FONT></TD>
					<TD><INPUT TYPE="text" NAME="mail" SIZE="30"></TD>
				</TR>
				<TR>
					<TD NOWRAP><FONT SIZE="2">�̿���</FONT></TD>
					<TD COLSPAN="3"><TEXTAREA NAME="note" COLS="53" rows="10"></TEXTAREA></TD>
				</TR>

				<TR>
					<TD ALIGN="center" COLSPAN="4">
						<INPUT TYPE="submit" NAME="send" VALUE="��������">��
						<INPUT TYPE="reset" VALUE="���ƥ��ꥢ">
					</TD>
				</TR>
			</TABLE>
		</TD>
	</TR>
</TABLE>
<P>
<FONT color="red">*</FONT>���դ������ܤ�����ɬ�ܹ��ܤǤ���
</P>
<FONT SIZE=2><I>
Copyright (C) 2001-2003 All right reserved by <A HREF="http://cgikon.com">CGI KON</A>
</I></FONT>
</CENTER>
</FORM>
</BODY>
</HTML>
!;

# Copyright (C) 2001-2003 All right reserved by Shinya Kondo ( CGI KON )
