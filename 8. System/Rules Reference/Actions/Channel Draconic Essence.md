---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You aren't channeling draconic essence and you're holding or wearing your draconic gift

**Effect** You call down a portion of the magical essence of your draconic benefactor. A Medium spectral dragon that looks like your benefactor appears in any square within 30 feet. This spectral dragon can't be targeted by any attacks or spells and has no Hit Points, saving throws, or skills. It can occupy the same space as creatures and objects. While your spectral dragon is in your space, you gain a +1 status bonus to saves against sleep and paralysis.

Channel Draconic Essence lasts until you Channel Draconic Essence again, you Dismiss the effect, the encounter ends, you fall [[Unconscious]], or the spectral dragon is farther than 120 feet from you, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
