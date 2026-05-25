---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 100, 'pp': 0, 'sp': 0}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can attach these light-brown leather flaps adorned with gold stitching to a breastplate or even clothing to protect your upper legs in battle. They give you the freedom to move your body to its limit without worrying about exposing yourself to a hit. While wearing the tasset of flexibility, you gain a +1 item bonus to Acrobatics checks.

**Activate—Lunging Attack** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The tasset helps you stretch farther than you normally could. Make a Strike with a melee weapon, increasing your reach by 5 feet for that Strike.

**Source:** `= this.source` (`= this.source-type`)
