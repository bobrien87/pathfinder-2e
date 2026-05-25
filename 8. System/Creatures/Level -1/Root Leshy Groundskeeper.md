---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Root Leshy Groundskeeper"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]]"
languages: "Common, Fey (speak with plants (root vegetables only))"
skills:
  - name: Skills
    desc: "Athletics +5, Nature +5, Stealth +4, Survival +5, Labor Lore +2"
abilityMods: ["+3", "+0", "+3", "-1", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +8, **Ref** +2, **Will** +5"
health:
  - name: HP
    desc: "9"
abilities_mid:
  - name: "Verdant Burst"
    desc: "When the root leshy groundskeeper dies, a burst of primal energy explodes from their body, restoring @Damage[1d4[healing,vitality]|shortLabel] Hit Points to each plant creature in a @Template[type:emanation|distance:30]. This area immediately fills with roots and vines, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shovel +5 (`pf2:1`) (fatal d10), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13, attack +0<br>**3rd** [[Speak with Plants (root vegetables only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The root leshy groundskeeper transforms into a Small root vegetable. This ability otherwise uses the effects of [[One with Plants]]. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Root in Place"
    desc: "`pf2:1` The root leshy groundskeeper roots themself into the ground, reducing their Speed to 0 and granting them a +1 circumstance bonus to AC and 2 temporary Hit Points until the start of their next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Hardy root leshies have the strength and stamina to dig furrows for planting seeds over long hours. Though they're humble even among leshies, they can be extremely stubborn even against powerful adversaries.

Nature spirits inhabit bodies made of plants or fungi, blooming from primal magic to become the small people called leshies. They come in a truly immense number of diverse shapes and sizes, more so than most peoples of Golarion. This variety of forms means a leshy could have a place in nearly any type of setting for any type of story.

```statblock
creature: "Root Leshy Groundskeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
