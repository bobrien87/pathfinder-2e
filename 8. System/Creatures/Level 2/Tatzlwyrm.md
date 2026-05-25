---
type: creature
group: ["Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tatzlwyrm"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dragon"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +8, Crafting +4, Intimidation +6, Stealth +7"
abilityMods: ["+4", "+1", "+3", "-3", "+2", "+0"]
abilities_top:
  - name: "Natural Camouflage"
    desc: "A tatzlwyrm's green, gray, and brown scales provide it natural camouflage. In areas of dense undergrowth, a tatzlwyrm can move at its full Speed when Sneaking, and it gains a +4 circumstance bonus to `act hide options=natural-camouflage`."
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "30; **Immunities** paralyzed, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, magical), **Damage** 1d6+6 slashing"
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (magical, unarmed), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Poison Gasp"
    desc: "`pf2:1` The tatzlwyrm belches a puff of poisonous vapor into the face of an adjacent creature, which must attempt a DC 15 [[Fortitude]] save; the creature takes a –2 circumstance penalty to this save if it's [[Grabbed]] or [[Off Guard]]. The tatzlwyrm can't use Poison Gasp again for 2 rounds. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Sickened]] 1. <br> - **Failure** The target takes 2d6 poison damage and is [[Enfeebled]] 1 for 1 round. <br> - **Critical Failure** The target takes 4d6 poison damage and is enfeebled 1 for 1 minute."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Tatzlwyrms resemble human-sized snakes with two arms and a dragon's head. Distant relatives of dragons, tatzlwyrms possess only a meager level of intelligence. They can speak Draconic (with a thick, hissing accent), but their ability to reason is limited, and they can't use magic. They do possess a level of cunning, however, and some have been known to build rudimentary traps and even lairs. They aren't treasure hoarders, though, so adventurers shouldn't expect to find a tatzlwyrm sitting atop a bed of coins.

Some tatzlwyrms have managed to forge working relationships with dragons, though it's a rare occurrence. From time to time, dragons have used them as messengers (because they can speak their language, however crudely), scouts (due to their smaller size), guides (when they're familiar with a particular mountain), and even muscle (harassing foes not worthy of a dragon's direct attention).

Tatzlwyrms hibernate in cold weather, and when they feel winter approaching, they seek out underground lairs, mountain crevices, or even hay lofts. On one notable occasion, villagers reported being briefly overrun by tatzlwyrms after a conflict between spellcasters in the nearby hills caused a sudden blizzard. Local scholars still debate whether the cause of the influx stemmed from the sudden change in weather or if the creatures were drawn to one of the other magic users staying in town who were part of the same pilgrimage as those doing battle.

When confronted, tatzlwyrms are more likely to attack than retreat. Indeed, they sometimes lie in wait on purpose, taking advantage of their scales' natural camouflage and awaiting the chance to unleash their signature move: belching poisonous vapor into an opponent's face. Since this breath attack doesn't have much range, tatzlwyrms usually need to grab their foes first to bring them close to their mouth.

```statblock
creature: "Tatzlwyrm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
