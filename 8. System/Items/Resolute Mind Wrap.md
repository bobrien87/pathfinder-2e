---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The followers of the Tan Sugi monastery understood the value of protecting the mind from the intrusion of violence and anger and infused this strip of striped green and brown cloth with their beliefs. Wrapped around the head, the stripes almost evoke the patterns of sugi branches coiled around the wearer's skull. The *resolute mind wrap* grants you mental resistance 5.

**Activate—Shield Thoughts** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You attempt a Will saving throw against a mental effect

**Effect** The *resolute mind wrap* clings more tightly to your head, granting you a +1 item bonus to your Will saving throw. If you succeed at this saving throw, the resistance to mental damage granted by the *resolute mind wrap* increases to 10 for 1 minute.

> [!danger] Effect: Resolute Mind Wrap

**Source:** `= this.source` (`= this.source-type`)
