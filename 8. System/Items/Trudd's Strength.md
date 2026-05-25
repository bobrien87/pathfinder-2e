---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Divine]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 160, 'pp': 0, 'sp': 0}"
usage: "etched-onto-clan-dagger"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This filigree depiction of a warhammer in front of a kite-shaped shield grants you a +1 item bonus to Athletics checks and to Intimidation checks to [[Coerce]]. Additionally, once per day, the filigree symbol can be activated to protect your allies.

**Activate—Protect the Clan!** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** Protective energy releases in a @Template[type:emanation|distance:10], granting a +1 status bonus to Armor Class to all allies within the area. The bonus lasts for 1 minute.

> [!danger] Effect: Trudd's Strength

**Source:** `= this.source` (`= this.source-type`)
