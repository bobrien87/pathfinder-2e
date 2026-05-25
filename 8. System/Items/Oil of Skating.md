---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thin, slippery oil shimmers with a golden hue. Coating your shoes or feet with oil of skating enables you to skate quickly along flat surfaces for 1 hour. You gain a +10-foot status bonus to your Speed, which doubles if you move on a downhill surface. You lose this bonus if moving on difficult terrain, greater difficult terrain, or uneven ground. Also, you treat any uphill movement as moving on difficult terrain while your feet are oiled and treat the results of any Acrobatics checks made to [[Balance]] as one degree worse.

**Source:** `= this.source` (`= this.source-type`)
