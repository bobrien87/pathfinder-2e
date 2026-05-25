---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Metal]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This shimmery metal cane is both an assistive device and a popular companion for many zuhras. The cane's possessor can spend 1 minute feeding the cane an elixir or a dose of ingested or injury poison to fill its venom sac. The cane can store only one such alchemical item at a time, and it expels the alchemical item when either 24 hours pass or it's fed a new alchemical item.

**Activate—Silver Snake Sword** `pf2:1` (concentrate, polymorph)

**Effect** The silver snake cane becomes a *+1 striking silver sword cane* for 10 minutes. If the cane holds a dose of poison with the injury trait, that poison is automatically applied to the weapon. If the poison hasn't been expended by the time the cane turns back to normal, it remains stored in the cane. You can Dismiss this activation.

**Activate—Silver Snake Serum** `pf2:1` (concentrate)

**Requirements** The silver snake cane holds a dose of an alchemical item

**Frequency** once per day

**Effect** The silver snake cane bites a willing target of your choice within your reach, dealing 1 piercing damage and injecting the alchemical item. The item is expended, and if it was an elixir or ingested poison, the target is affected as though it consumed the item.

**Activate—True Silver Snake** `pf2:1` (concentrate)

**Prerequisites** You're a zuhra

**Effect** The cane transforms into a giant viper made of silver. All its Strikes are silver. It acts independently but obeys you. You can Dismiss this activation.

**Source:** `= this.source` (`= this.source-type`)
