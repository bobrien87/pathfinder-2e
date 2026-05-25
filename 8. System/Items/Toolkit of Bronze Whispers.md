---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Divine]]", "[[Intelligent]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +12; precise vision 30 feet, imprecise hearing 30 feet

**Communication** telepathy (Common and two other common languages)

**Skills** Clockwork Lore +15, Crafting +13, Religion +11

**Int** +4, **Wis** +3, **Cha** +0

**Will** +12

Sacred to the faith of Brigh, a toolkit of bronze whispers has been used with such devotion it has developed a consciousness and personality that can be a blessing to a partnered crafter. A toolkit of bronze whispers functions as a set of Artisan's Tools (Sterling). Such toolkits focus on new creations and enthusiastically suggest crafting techniques to wielders. A toolkit of bronze whispers knows common item formulas of its level or lower and any other formulas the GM chooses. It can teach these formulas. You must still spend the time to copy a formula before you can use it.

**Source:** `= this.source` (`= this.source-type`)
