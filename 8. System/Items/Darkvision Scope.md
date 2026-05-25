---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 160}"
usage: "attached-to-crossbow-or-firearm-firing-mechanism"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These scopes, popular with snipers and other sneaky sharpshooters who ply their trade in the dead of night, incorporate clouded crystals with magical properties into their design. While relatively useless under normal lighting conditions, these crystals can help bring things into focus when used in dim light. The scope is then given an enchantment to enhance these properties for use in darkness. The scope grants you a +1 item bonus to Perception checks involving sight in areas of dim light visible through the scope (as well as in areas of darkness, if the scope has been activated).

**Activate—See Through Night** `pf2:1` (manipulate)

**Effect** You gain darkvision until the beginning of your next turn, as long as you continue to look through the scope.

**Source:** `= this.source` (`= this.source-type`)
