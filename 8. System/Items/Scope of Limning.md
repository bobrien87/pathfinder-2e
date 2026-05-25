---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "attached-to-firearm-scope"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The dwarven gunsmiths of Dongun Hold originally created these scopes to help them clear out vermin in underground areas. This scope captures the sound that echoes off a creature hit by the firearm and transforms it into light, illuminating the target for all to see.

**Activate—Outline** `pf2:1` (auditory, light, manipulate)

**Effect** If your next Strike from the weapon to which the scope is attached hits a creature, the sound of the impact transforms into light, causing the creature to glow until the end of your next turn. A visible creature can't be [[Concealed]] while they glow. If a creature is [[Invisible]], they're concealed while glowing, rather than being undetected. Because the effect requires a solid impact, incorporeal creatures are unaffected unless the bullet can deal force damage or has the effects of the ghost touch property rune.

**Source:** `= this.source` (`= this.source-type`)
