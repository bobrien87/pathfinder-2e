---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Artifact]]", "[[Primal]]"]
price: "{'value': {}}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved from a scale of the kaiju Igroon, this jagged shield refracts light around it in a shimmering haze. A scale of Igroon (Hardness 20, HP 160, BT 80) recovers 4 Hit Points at the start of its wielder's turn. When you [[Raise a Shield]], you can use the [[Shield Block]] reaction with the *scale of Igroon* to block an attack or effect that deals acid, cold, electricity, fire, force, or sonic damage as well as physical damage.

**Activate** `pf2:1` (manipulate)

**Requirements** You're in an area of bright or dim light

**Effect** You angle the shield to refract light. Until the start of your next turn, you gain a +4 item bonus to Stealth checks to [[Hide]] and [[Sneak]] and can do so while observed. This bonus ends if you Activate another ability or use the Shield Block reaction.

**Activate** `pf2:1` (manipulate)

**Requirements** You're in an area of bright light

**Effect** You angle the shield at a target within 60 feet, reflecting light into its eyes. It must attempt a DC 42 [[Fortitude]] save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Blinded]] until its next turn begins.
- **Failure** The target is blinded for 1 minute.
- **Critical Failure** The target is blinded for 2d4 hours.

**Activate** `pf2:f` (manipulate)

**Trigger** You use Shield Block and prevent yourself from taking energy damage from a line, ray, or a direct attack, including a [[Force Barrage]] spell

**Effect** You reflect the energy along a trajectory you choose. The effect travels only up to its remaining range, using its original parameters if it strikes other targets.

**Destruction** If a deity, kaiju, spawn of a deity, titan, or being of similar power stomps on a scale of Igroon while in absolute darkness, the shield is destroyed permanently.

**Source:** `= this.source` (`= this.source-type`)
