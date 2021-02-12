import twint

twi = twint.Config()
twi.Search = 'vaksin corona'
twi.Lang = 'in'
Pandas = True
twi.Until = '2020-12-20'
twi.Since = '2020-12-13'
twi.Custom["tweet"] = ["id", "date", "username", "tweet"]
twi.Limit = 2500
twi.Output = "vaksin.csv"
twi.Store_csv = True
twint.run.Search(twi)
