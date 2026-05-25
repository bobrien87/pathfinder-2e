---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dynamo"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +18, Crafting +17, Medicine +16, Thievery +17, Engineering Lore +17"
abilityMods: ["+6", "+3", "+2", "+3", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +14, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "145"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Modular Prosthesis +20 (`pf2:1`), **Damage** 2d8+12 bludgeoning"
  - name: "Ranged strike"
    desc: "Dragon Mouth Pistol +18 (`pf2:1`) (concussive, reload 1, scatter 5, range 20 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Extend Arms"
    desc: "`pf2:1` The dynamo extends their collapsible steel arms, giving them both a reach of 20 feet with all melee attacks. However, the dynamo becomes [[Enfeebled]] 1 and can't use the Interact action. The dynamo can Dismiss this ability."
  - name: "Extend Legs"
    desc: "`pf2:1` The dynamo rises into the air on 10-foot-tall telescoping steel legs. While their legs are extended, the dynamo gains a +10-foot status bonus to land Speed and ignores any cover granted by barriers less than 10 feet tall. However, the dynamo becomes [[Clumsy]] 1 and can't use the Climb, [[Leap]], Swim, or [[Tumble Through]] actions. The dynamo can Dismiss this ability."
  - name: "Modular Prostheses"
    desc: "`pf2:1` The dynamo configures one or both of their mechanical prosthetic hands into a specific configuration. Each configuration deals a specific damage type and has its own weapon traits: fist (bludgeoning; free-hand), gaff hook (piercing; grapple), impact driver (bludgeoning; shove), or spinning blade (slashing; trip). The dynamo can alternatively transform a hand into a steel shield with Hardness 8, HP 72, and BT 36. A broken prosthesis can't be reconfigured until repaired."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The intricate clockwork prostheses known as sterling dynamos have become increasingly common in recent years, particularly in havens of technological progress like Dongun Hold and the city of Absalom, but a few specialized engineers have elevated their dedication to research and development of such devices to an entirely new level. These individuals seek to achieve bodily perfection through augmentation, replacing their own limbs with advanced and sometimes untested prototypes that grant them a wide variety of abilities.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Dynamo"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
