---
type: creature
group: ["Fey", "Gremlin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grimple"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: "Sakvroth"
skills:
  - name: Skills
    desc: "Crafting +5, Deception +2, Nature +4, Stealth +5, Thievery +5"
abilityMods: ["+1", "+3", "+3", "+1", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +5, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "9; **Weaknesses** cold iron 2"
abilities_mid:
  - name: "Gremlin Lice"
    desc: "Whenever a living creature touches or is touched by a grimple (including via a successful unarmed melee Strike), it must succeed at a DC 13 [[Reflex]] save or become infested by gremlin lice. <br>  <br> While infested, the targeted creature is distracted by the itching sensation and is [[Stupefied 1]], though it can use an Interact action to scratch at the itching lice to suppress the stupefied condition from the lice for 1d4 rounds. <br>  <br> The infestation ends after 24 hours or until the creature is submerged in water or exposed to a severe cold environment, whichever comes first."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +7 (`pf2:1`) (agile, finesse), **Damage** 1d4 + 1 piercing plus [[Gremlin Lice]]"
  - name: "Ranged strike"
    desc: "Rock +7 (`pf2:1`) (agile, range 20 ft.), **Damage** 1d4 + 1 bludgeoning plus [[Rock]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**1st** [[Grease]], [[Prestidigitation]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Putrid Vomit"
    desc: "`pf2:1` The grimple spews a @Template[type:line|distance:30] of vomit. Each creature in the line must succeed at a DC 16 [[Fortitude]] save or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure). The grimple can't use Putrid Vomit again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Even more than most gremlins, grimples resent the trappings of civilization: inn common rooms with their rowdy singalongs, livery yards with their whinnying horses, church steeples with their clanging bells. Grimples live to spoil these conventions, dropping tavern signs on patrons, urinating in rain barrels, and opening stable doors. When all else fails, they literally vomit their disdain on passersby.

Grimples resemble humanoid, mange-ridden opossums, with boar-like tusks that aid them in rooting through garbage heaps for food. They're agile climbers who glide from eave to eave on the loose flaps of skin between their limbs. Savvy gremlin-hunters know to look for the skin flakes and fur grimples shed from their parasite-infested hides.

Gremlins arose long ago in the First World, living embodiments of nature's ability to wear away, erode, and decompose. In the Universe, their encounters with mortal civilizations twisted them into creatures devoted to chaos, sabotage, and traps, each variety specializing in a particular brand of mayhem.

```statblock
creature: "Grimple"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
