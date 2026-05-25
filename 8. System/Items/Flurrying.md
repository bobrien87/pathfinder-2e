---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 360}"
usage: "etched-onto-melee-weapon-monk"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you make a Flurry of Blows using the etched weapon and your first Strike reduces a creature to 0 Hit Points, you can make your second Strike with an echo of the weapon, increasing the reach to 30 feet.

**Activate** `pf2:2` (concentrate, force)

**Frequency** once per day

**Effect** The weapon casts a [[Spiritual Armament]] spell. The ghostly weapon looks like the etched weapon. Use your normal attack bonus and damage for the weapon instead of the damage listed in the spell, but use your Wisdom modifier instead of Strength when determining damage. You can choose to make a Flurry of Blows instead of a Strike when the *spiritual armament* attacks; this still counts as your flourish for the turn. You can Sustain this activation in the same manner as the spell.

**Source:** `= this.source` (`= this.source-type`)
