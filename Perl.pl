use strict;
use warnings;

my $filename = 'article.txt';
open(my $fh, '<:encoding(UTF-8)',$filename)
	or die "Could not open file";
my %words_count;
while(my $line = <$fh>) {
	my @words = split / /, $line;
	foreach my $word (@words) {
		$word =~ s/[.,\p{Pi}\p{Pf}"]//g;
		$word = lc $word;
		$words_count{$word}++;
	}
}

foreach my $word (reverse sort {$words_count{$a} <=> $words_count{$b}} keys %words_count) {
	printf "%-31s %s\n",$word,$words_count{$word};
}
