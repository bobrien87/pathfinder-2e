---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kuribu"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +11, Diplomacy +8, Religion +9, Stealth +9"
abilityMods: ["+2", "+4", "+1", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "45; **Weaknesses** unholy 5"
abilities_mid:
  - name: "Immobilizing Ambush"
    desc: "`pf2:r` **Requirements** The kuribu is disguised as a statue <br>  <br> **Trigger** A creature moves within 60 feet of the kuribu <br>  <br> **Effect** The kuribu springs into action by making a shortbow Strike against the triggering creature. If the Strike hits, the creature is pinned by the arrow, as described in the bow critical specialization."
  - name: "Sentinel's Aura"
    desc: "30 feet. The kuribu and any other creature in the aura defending the same holy site gain a +1 status bonus to AC. This aura is suppressed while Statue is in effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, holy, magical), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +11 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Blessed Aspect"
    desc: "`pf2:2` The kuribu's face transforms, and their holy countenance unleashes an attack based on the aspect the kuribu chooses. The kuribu can't use Blessed Aspect again for 1d4 rounds. They can revert back to their humanoid appearance at any time, but they still have to wait before using Blessed Aspect again. <br>  <br> - **Eagle** The kuribu unleashes a disorienting screech in a @Template[type:cone|distance:15] that deals @Damage[2d10[sonic]|options:area-damage] damage with a DC 19 [[Will]] save. A creature that critically fails is also [[Stunned]] 1. <br> - **Lion** The kuribu makes a powerful jaws Strike against an adjacent creature. The attack has a Kuribu jaws attack check{+12} attack modifer and deals @Damage[4d6[piercing],1d4[bleed]]{4d6 piercing damage plus 1d4 persistent bleed damage}. <br> - **Ox** The kuribu charges into a creature. The kuribu Flies or Strides. At the end of their movement, the kuribu crashes into one adjacent creature, dealing @Damage[4d6[bludgeoning]|options:area-damage] damage to it with a DC 17 [[Fortitude]] save. If the target critically fails, it's also knocked [[Prone]]."
  - name: "Statue"
    desc: "`pf2:1` Until the next time they act, the kuribu appears to be a statue. They have an automatic result of 29 on Deception checks and DCs to pass as a statue."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Kuribus serve as the guardians of temples and other holy sites. They are humanoid in appearance and roughly the size of human children. Their bodies look like stone, which allows kuribus to disguise themselves as statues for extended periods of time (sometimes up to centuries). When defending their sites, kuribus harry invaders from a distance.

```statblock
creature: "Kuribu"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
