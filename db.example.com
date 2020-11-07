$TTL 1d
$ORIGIN example.com.

@	IN	SOA	ns1.	root.(
		20180904	;Serial
		12h		;Refresh
		15m		;Retry
		3w		;Expire
		2h		;Minimum
	)
example.com. IN NS ns1.
www.example.com. IN A 127.0.0.5
sub1.exapmle.com IN A 127.0.0.8
