import twint

twi = twint.Config()
twi.Search = 'dukung vaksin corona'
twi.Lang = 'in'
twi.Until = '2021-02-18'
twi.Since = '2021-01-13'
Limit = 1000
Pandas = True
twi.Custom["tweet"] = ["id", "date", "username", "tweet"]
twi.Output = "vaksin2.csv"
twi.Store_csv = True
twint.run.Search(twi)
