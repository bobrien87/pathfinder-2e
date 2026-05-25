---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Magical monkey spirits fill the area as they pile and climb on top of one another. Because the monkeys are magical spirits, they can't be attacked or hurt. Casting [[Calm]] or a similar effect over the monkeys makes them docile, causing them to cease making mischief for the duration of *mad monkeys*.

Choose the kind of mischief your monkeys make when you Cast the Spell. They produce the effect listed for that mischief when you Cast the Spell and the first time each round when you Sustain the Spell. The first time each round when you Sustain the Spell, you can move the area of the monkeys by 5 feet.

**Flagrant Burglary** The monkeys try to [[Steal]] any one item from one creature in the area. Use your spell DC - 10 as the monkeys' Thievery modifier. Their attempt relies more on distraction than subtlety, so the victim knows what item the monkeys were trying to take and whether it was taken. Getting a stolen item from the monkeys-even for the caster-requires Stealing it from them or [[Disarming]] them, using your spell DC. When the spell ends, any stolen items fall to the ground in any square of the spell's area you choose.

**Raucous Din** The monkeys screech loudly, potentially deafening creatures in the spell's area. Each creature in the spell's area must attempt a Fortitude save.
- **Critical Success** The creature is unaffected and is temporarily immune for 10 minutes.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Deafened]] for 1 round.
- **Critical Failure** The creature is Deafened for 1 minute.

**Tumultuous Gymnastics** The monkeys jump and climb all over creatures in the spell's area, interfering with complex movements. Each creature in the spell's area must attempt a Reflex save.
- **Critical Success** The creature is unaffected and is temporarily immune for 10 minutes.
- **Success** The creature is unaffected.
- **Failure** For 1 round, the creature must succeed at a DC 5 flat check whenever it attempts a manipulate action. If it fails this check, the creature loses that action.
- **Critical Failure** As failure, but the monkeys cling to the creature tenaciously, and the effect lasts until the spell ends, even if the creature leaves the spell's area.

**Source:** `= this.source` (`= this.source-type`)
