---
type: creature
group: ["Aberration", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skittering Slayer"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +17, Intimidation +15, Stealth +16"
abilityMods: ["+5", "+4", "+6", "+0", "+3", "+3"]
abilities_top:
  - name: "Clinging Remnants"
    desc: "A swarm strider's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 2d4 persistent,piercing damage."
armorclass:
  - name: AC
    desc: "26 all-around vision; **Fort** +18, **Ref** +16, **Will** +13"
health:
  - name: HP
    desc: "130; **Immunities** precision, swarm mind; **Weaknesses** area damage 10, splash damage 10; **Resistances** physical 5, poison 5"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Agitated by Light"
    desc: "When exposed to bright light, the skittering slayer must attempt a DC 25 [[Will]] save. On a failure, they become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure). The skittering slayer then becomes immune to being agitated by light for 10 minutes."
  - name: "Discorporate"
    desc: "When the swarm strider is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the swarm strider can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the swarm strider permanently. The invertebrates have a collective pool of 32 HP, and the same AC, saves, immunities, resistances, and weaknesses as the swarm strider. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the swarm strider."
  - name: "Scatter"
    desc: "`pf2:r` **Trigger** The skittering slayer is targeted by a splash attack or would attempt a Reflex save against an area effect <br>  <br> **Effect** The skittering slayer scatters in place, gaining a +2 circumstance bonus to AC and Reflex saves against the triggering effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flail +20 (`pf2:1`) (disarm, reach 10 ft., sweep, trip), **Damage** 2d6+11 bludgeoning plus [[Clinging Remnants]]"
  - name: "Melee strike"
    desc: "Light Hammer +19 (`pf2:1`) (agile, reach 10 ft.), **Damage** 1d6+11 bludgeoning plus [[Clinging Remnants]]"
  - name: "Melee strike"
    desc: "Light Hammer +19 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+11 bludgeoning plus [[Clinging Remnants]]"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, finesse, nonlethal, reach 10 ft., unarmed), **Damage** 1d4+11 bludgeoning plus [[Clinging Remnants]]"
spellcasting: []
abilities_bot:
  - name: "Draw Bugs"
    desc: "`pf2:1` The swarm strider draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 10 HP. At the GM's discretion, the swarm strider doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Squirming Embrace"
    desc: "`pf2:1` The swarm strider Strides. If they end their movement sharing a space with a creature, they deal 3d6 piercing damage to the creature, with a DC 26 [[Reflex]] save. The swarm strider can Burrow, Climb, Fly, or Swim instead of Striding if they have the corresponding movement type."
  - name: "Swarm Shape"
    desc: "`pf2:1` The swarm strider collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession. In this form, the swarm strider can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to Squeeze. They can use the same action to coalesce from their swarm shape back into their normal form."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When a warrior's last thoughts are of bloodlust, their body can become so suffused with rage that it infects whatever eats their corpse. This singular emotion binds together the resultant swarm, combining the insects' will to survive with a berserker's deathless rage, creating an indomitable combatant. Often made of roaches or similarly tenacious insects, skittering slayers rarely develop long-term plans, instead scuttling about in search of dark refuges and passionate fights. These swarm striders tend to avoid transforming into their swarm shape, preferring to face their foes directly whenever possible.

All living creatures eventually become worm food. Yet if a creature perishes while gripped by overwhelming emotion or unfinished business, its flesh can become infused with those obsessions or a simple refusal to perish, infecting whatever detritivores feast on the body. As they feast, the invertebrates awaken to a type of collective intelligence, including some of the dead creature's memories and motivations. Once the body is stripped bare, the vermin swarm together and intertwine to recreate the dead creature's form out of thousands of wriggling bodies. These reborn are known as swarm striders.

Though many swarm striders are accidental creations, a few rare mortals purposefully transform themselves into swarm striders through powerful rituals. Most often, this process involves specially preparing a grave with ample scavengers and enchanting the site with occult magic to anchor their soul until it can live within the swarm. Through transformation, these intentional swarm striders seek out the power to slip past any defense or claim the virtual immortality of an ever-regenerating horde, as a swarm strider can reconstitute their form from even a single worm. However, the transformation inevitably scars the creature—often causing emotional detachment, the disintegration of old taboos, and a dissociated sense of self now that one mind has become a thousand. In their transformed state, even the best-intentioned swarm strider might embrace villainy and lose any semblance of their former selves over the span of many years.

```statblock
creature: "Skittering Slayer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
