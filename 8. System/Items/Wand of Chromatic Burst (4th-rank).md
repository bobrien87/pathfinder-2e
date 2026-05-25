---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Light]]", "[[Magical]]", "[[Manipulate]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This intricately carved quartz wand changes color, cycling through the colors of the rainbow.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 4th-rank [[Chromatic Armor]]. Additionally, the target can use the Chromatic Armor Burst action.

**Chromatic Armor Burst** `pf2:1` (concentrate, light, magical)

**Requirements** You're affected by [[Chromatic Armor]] created by the *wand of chromatic burst*

**Effect** Choose one color of the [[Chromatic Armor]] the wand created for you. The spell ends and light of that color flashes brightly in a @Template[emanation|distance:20]. Creatures in the area take 4d6 untyped damage of the type associated with the color you chose, with a [[Reflex]] save against your spell DC. This action has the trait corresponding to the damage type you chose.

**Craft Requirements** Supply a casting of [[Chromatic Armor]] of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
