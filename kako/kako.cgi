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
	<TITLE>加古宜士先生、古希お祝い会参加申し込み</TITLE>
	<META Http-Equiv="Content-Type" Content="text/html;charset=EUC-JP">
</HEAD>
<BODY>
<CENTER>
<TABLE BORDER="0" BGCOLOR="#EEEEEE" CELLPADDING="20" WIDTH="60%">
	<TR>
		<TD ALIGN="center">
			<FONT SIZE="4"><B>加古宜士先生、古希お祝い会参加申し込み</B></FONT>
		</TD>
	</TR>
	<TR>
		<TD ALIGN="center">
			<P>
			<FONT COLOR="#FF0000">入力項目が不完全です</FONT>
		</TD>
	</TR>
</TABLE>
</CENTER>
</BODY>
</HTML>
!;
}

# メインプログラム

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
			$record .= sprintf("%04d年%02d月%02d日,",$year,$mon,$mday);
			$record .= sprintf("%02d時%02d分%02d秒\n",$hour,$min,$sec);
			print OFILE jcode($record)->sjis;
			close(OFILE);
			$info = "送信が完了しました。";
		} else {
			$error = "送信できませんでした。";
		}

		require "member_1.tmpl";
		exit;
	}

# 会員登録フォームの表示

print "Content-type: text/html\n\n";
print qq!
<HTML>
<HEAD>
	<TITLE>加古宜士先生、古希お祝い会参加申し込み</TITLE>
	<META Http-Equiv="Content-Type" Content="text/html;charset=EUC-JP">
</HEAD>
<BODY>
<FORM ACTION="kako.cgi" METHOD="post">
<CENTER>
<TABLE BORDER="0" BGCOLOR="#EEEEEE" CELLPADDING="10">
	<TR>
		<TD ALIGN="center">
			<FONT SIZE="4"><B>加古宜士先生、古希お祝い会参加申し込み</B></FONT>
			<P>
			<FONT SIZE="2">※ 以下の項目に入力し、「送信する」をクリックして下さい。</FONT><BR>
			<FONT COLOR="#FF0000"></FONT><BR>
			<TABLE BORDER="0" CELLPADDING="3">
				<TR>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">御芳名</FONT></TD>
					<TD><INPUT TYPE="text" NAME="name" SIZE="30"></TD>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">フリガナ</FONT></TD>
					<TD><INPUT TYPE="text" NAME="kana" SIZE="30"></TD>
				</TR>
<TR>
<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">郵便番号</FONT></TD>
					<TD><INPUT TYPE="text" NAME="postal" SIZE="9"></TD>
</TR>
				<TR>
					<TD NOWRAP><FONT color="red">*</FONT><FONT SIZE="2">御住所</FONT></TD>
					<TD COLSPAN="3">
						<SELECT NAME="add1">
							<OPTION>北海道
							<OPTION>青森県
							<OPTION>岩手県
							<OPTION>宮城県
							<OPTION>秋田県
							<OPTION>山形県
							<OPTION>福島県
							<OPTION>茨城県
							<OPTION>栃木県
							<OPTION>群馬県
							<OPTION>埼玉県
							<OPTION>千葉県
							<OPTION selected="selected">東京都
							<OPTION>神奈川県
							<OPTION>山梨県
							<OPTION>長野県
							<OPTION>新潟県
							<OPTION>富山県
							<OPTION>石川県
							<OPTION>福井県
							<OPTION>岐阜県
							<OPTION>静岡県
							<OPTION>愛知県
							<OPTION>三重県
							<OPTION>滋賀県
							<OPTION>京都府
							<OPTION>大阪府
							<OPTION>兵庫県
							<OPTION>奈良県
							<OPTION>和歌山県
							<OPTION>鳥取県
							<OPTION>島根県
							<OPTION>岡山県
							<OPTION>広島県
							<OPTION>山口県
							<OPTION>徳島県
							<OPTION>香川県
							<OPTION>愛媛県
							<OPTION>高知県
							<OPTION>福岡県
							<OPTION>佐賀県
							<OPTION>長崎県
							<OPTION>熊本県
							<OPTION>大分県
							<OPTION>宮崎県
							<OPTION>鹿児島県
							<OPTION>沖縄県
						</SELECT>
					<INPUT TYPE="text" NAME="add2" SIZE="58">
					</TD>
				</TR>
				<TR>
					<TD NOWRAP><FONT SIZE="2">御電話番号</FONT></TD>
					<TD><INPUT TYPE="text" NAME="tels" SIZE="30"></TD>
					<TD NOWRAP><FONT SIZE="2">E-mail</FONT></TD>
					<TD><INPUT TYPE="text" NAME="mail" SIZE="30"></TD>
				</TR>
				<TR>
					<TD NOWRAP><FONT SIZE="2">通信欄</FONT></TD>
					<TD COLSPAN="3"><TEXTAREA NAME="note" COLS="53" rows="10"></TEXTAREA></TD>
				</TR>

				<TR>
					<TD ALIGN="center" COLSPAN="4">
						<INPUT TYPE="submit" NAME="send" VALUE="送信する">　
						<INPUT TYPE="reset" VALUE="内容クリア">
					</TD>
				</TR>
			</TABLE>
		</TD>
	</TR>
</TABLE>
<P>
<FONT color="red">*</FONT>の付いた項目は入力必須項目です。
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
