---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 90}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A good pair of gloves is a critical item for any soldier, particularly if you plan to get up close to your enemy. When you wear these black leather gloves with fine silver stitching, you gain a +1 item bonus to Athletics checks to [[Climb]], [[Grapple]], and [[Reposition]].

**Activate—Sticky Grip** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** You have an enemy [[Grabbed]] or [[Restrained]]

**Effect** Your gloves help you squeeze even more tightly, keeping your opponent from moving freely. The enemy you have grabbed or restrained is [[Slowed]] 1 for 1 round.

**Source:** `= this.source` (`= this.source-type`)
