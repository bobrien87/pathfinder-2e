---
type: creature
group: ["Aberration", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Thousand Thieves"
level: "16"
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
    desc: "+29; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: "Aklo, Common, Sakvroth, Shadowtongue"
skills:
  - name: Skills
    desc: "Acrobatics +30, Deception +28, Occultism +26, Society +28, Stealth +32, Thievery +32, Underworld Lore +30"
abilityMods: ["+4", "+8", "+7", "+6", "+5", "+2"]
abilities_top:
  - name: "Clinging Remnants"
    desc: "A swarm strider's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 4d4 persistent,piercing damage."
  - name: "Liquid Delirium"
    desc: "**Saving Throw** DC 37 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 4d6 poison and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 4d6 poison and [[Stupefied 2]] (1 round) <br>  <br> **Stage 3** 4d6 poison, stupefied 2, and [[Fascinated]] by a random object (1 round) <br>  <br> **Stage 4** [[Unconscious]] with no Perception check to wake up (1 round)"
  - name: "Sneak Attack"
    desc: "The thousand thieves Strikes deal an additional 3d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "40 all-around vision; **Fort** +25, **Ref** +31, **Will** +27"
health:
  - name: HP
    desc: "220; **Immunities** precision, swarm mind; **Weaknesses** area damage 15, splash damage 15; **Resistances** physical 15, poison 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Discorporate"
    desc: "When the swarm strider is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the swarm strider can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the swarm strider permanently. The invertebrates have a collective pool of 55 HP, and the same AC, saves, immunities, resistances, and weaknesses as the swarm strider. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the swarm strider."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +32 (`pf2:1`) (agile, finesse, versatile s), **Damage** 3d4+10 piercing plus [[Clinging Remnants]] plus [[Liquid Delirium]]"
  - name: "Melee strike"
    desc: "Dagger +32 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 3d4+10 piercing plus [[Clinging Remnants]] plus [[Liquid Delirium]]"
  - name: "Melee strike"
    desc: "Fist +32 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning plus [[Clinging Remnants]] plus [[Liquid Delirium]]"
  - name: "Ranged strike"
    desc: "Vermin Dart +30 (`pf2:1`) (range 40 ft.), **Damage** 3d8+10 piercing plus [[Clinging Remnants]] plus [[Liquid Delirium]]"
spellcasting: []
abilities_bot:
  - name: "Draw Bugs"
    desc: "`pf2:1` The swarm strider draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 20 HP. At the GM's discretion, the swarm strider doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Scuttling Shift"
    desc: "`pf2:2` The thousand thieves reverts to a swarm using Swarm Getaway, Sneaks up to their Speed, coalesces into their normal form, and Hides. This movement doesn't trigger reactions."
  - name: "Squirming Injection"
    desc: "`pf2:1` The swarm strider Strides. If they end their movement sharing a space with a creature, they deal 6d6 piercing damage to the creature, with a DC 37 [[Reflex]] save and exposing the target to liquid delirium. The swarm strider can Burrow, Climb, Fly, or Swim instead of Striding if they have the corresponding movement type."
  - name: "Swarm Getaway"
    desc: "`pf2:1` The thousand thieves collapses into a shapeless swarm of their constituent creatures. They drop all but up to 3 Bulk of held, worn, or carried objects in their possession. <br>  <br> In this form, the thousand thieves can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to Squeeze. They can use the same action to coalesce from their swarm shape back into their normal form. <br>  <br> As the swarm moves, the thousand thieves carries these objects if they can fit through the spaces the swarm moves through. The thousand thieves automatically dons any of the objects they desire when they reform. If the thousand thieves is [[Hidden]], Swarm Getaway doesn't reveal their location."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Good help is hard to find. For a master thief unable to find competent accomplices, sometimes the only way to execute the perfect heist involves becoming an entire guild of tiny creatures. Those who purposefully transform in this way favor scuttling creatures such as centipedes or spiders. On occasion, a thousand thieves instead forms when a community of pack rats discovers a dead scoundrel's body and fights over his ill-gotten gains. These swarm striders make use of their swarm form to enter homes, vaults, and other targets with ease.

All living creatures eventually become worm food. Yet if a creature perishes while gripped by overwhelming emotion or unfinished business, its flesh can become infused with those obsessions or a simple refusal to perish, infecting whatever detritivores feast on the body. As they feast, the invertebrates awaken to a type of collective intelligence, including some of the dead creature's memories and motivations. Once the body is stripped bare, the vermin swarm together and intertwine to recreate the dead creature's form out of thousands of wriggling bodies. These reborn are known as swarm striders.

Though many swarm striders are accidental creations, a few rare mortals purposefully transform themselves into swarm striders through powerful rituals. Most often, this process involves specially preparing a grave with ample scavengers and enchanting the site with occult magic to anchor their soul until it can live within the swarm. Through transformation, these intentional swarm striders seek out the power to slip past any defense or claim the virtual immortality of an ever-regenerating horde, as a swarm strider can reconstitute their form from even a single worm. However, the transformation inevitably scars the creature—often causing emotional detachment, the disintegration of old taboos, and a dissociated sense of self now that one mind has become a thousand. In their transformed state, even the best-intentioned swarm strider might embrace villainy and lose any semblance of their former selves over the span of many years.

```statblock
creature: "Thousand Thieves"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
