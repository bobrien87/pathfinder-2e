---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]", "[[Manipulate]]"]
prerequisites: "whose cry is thunder or dancer in the seasons"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You hold your arms out, and the fury of the seasons comes to your jubilant embrace. A storm spirals out from you, dealing 5d8 damage (see below) to each creature in a @Template[type:emanation|distance:30], with a [[Reflex]] save against your class DC. At 10th level and every 2 levels thereafter, the damage increases by 1d8.

The emanation is quartered into four non-overlapping cones, each of a different season, which must be arranged clockwise from spring, to summer, to fall, to winter. Each cone has different traits, damage type, and a different effect to a creature that critically fails its saving throw; a creature large enough to be in multiple seasons can choose which it is affected by.

- **Spring** (electricity) Spring lightning deals @Damage[(ceil((1+@actor.level)/2))d8[electricity]|options:area-damage|traits:electricity]{electricity damage}. Creatures who critically fail are left numb, becoming [[Clumsy]] 2 until the end of their next turn.
- **Summer** (water) A summer monsoon deals @Damage[(ceil((1+@actor.level)/2))d8[bludgeoning]|options:area-damage|traits:water]{bludgeoning damage}. Creatures who critically fail are knocked [[Prone]] by hurricane winds.
- **Fall** (emotion, mental, wood) Falling leaves deal @Damage[(ceil((1+@actor.level)/2))d8[slashing]|options:area-damage|traits:emotion,mental,wood]{slashing damage}. Creatures who critically fail are gripped by melancholy, becoming [[Off Guard]] until the end of their next turn.
- **Winter** (cold) A blizzard deals @Damage[(ceil((1+@actor.level)/2))d8[cold]|options:area-damage|traits:cold]{cold damage}. Creatures who critically fail are [[Stupefied 2]] until the end of their next turn as the cold numbs their senses.

**Source:** `= this.source` (`= this.source-type`)
