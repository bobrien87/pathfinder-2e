---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'sp': 1}"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Firearms require ammunition consisting of a projectile and black powder. A round of ammo can vary in its composition but is typically either a prepackaged paper cartridge, including wadding, bullet, and black powder, or loose shot packed in manually. Some weapons, like hand cannons and blunderbusses, can fire other materials, but their ammunition has the same Price due to the cost of the black powder. Because making rounds of firearm ammunition requires creating black powder, you need the [[Alchemical Crafting]] skill feat to make them. Firearm rounds are a valid option for magical ammunition, just like arrows or bolts. Crafting magical firearm ammunition requires you to be able to craft both alchemical and magical items.

**Source:** `= this.source` (`= this.source-type`)
