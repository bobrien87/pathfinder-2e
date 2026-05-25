---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Adamant Sentinel"
level: "18"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +38"
abilityMods: ["+9", "-1", "+9", "-5", "+0", "-5"]
abilities_top:
  - name: "Destructive Strike"
    desc: "On a critical hit, the adamant sentinel's fist Strike breaks the target's armor, if any, in addition to dealing damage to the target. If the target has a shield raised, the sentinel breaks the shield instead."
armorclass:
  - name: AC
    desc: "42; **Fort** +33, **Ref** +27, **Will** +29"
health:
  - name: HP
    desc: "255; repair mode; **Resistances** physical 20 except vorpal adamantine, spells 20"
abilities_mid:
  - name: "Repair Mode"
    desc: "When the adamant sentinel is at 0 HP, it isn't destroyed. Instead, it enters repair mode, during which it's [[Slowed]] 1, can't take reactions, and can take only the Self-Repair action. Once it has more than 30 HP, it can use any type of action and can use reactions, though it remains slowed 1 and can't take any reactions until the start of its next turn. If a critical hit with a [[Vorpal]] adamantine weapon reduces the sentinel to 0 HP, or if such a weapon hits it while it's already at 0 HP, the sentinel is destroyed."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +35 (`pf2:1`) (deadly 3d12, magical, reach 15 ft.), **Damage** 3d10+17 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Inexorable March"
    desc: "`pf2:1` The adamant sentinel Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can try to bar the way by attempting a DC 45 [[Fortitude]] save. <br> - **Critical Success** The sentinel halts its movement and cannot enter the creature's square. <br> - **Success** As critical success, but the resisting creature takes @Damage[(3d10+17)[bludgeoning]] damage. <br> - **Failure** The resisting creature takes @Damage[(3d10+17)[bludgeoning]] damage, and its armor, if any, is broken. If the resisting creature has a shield raised, the sentinel breaks the shield instead."
  - name: "Self-Repair"
    desc: "`pf2:1` The sentinel repairs itself, regaining 30 healing Hit Points."
  - name: "Vent"
    desc: "`pf2:1` The sentinel vents a @Template[type:cone|distance:30] of superheated steam from its internal forge. This deals @Damage[15d6[fire]|options:area-damage] damage to all creatures in the cone (DC 40 [[Reflex]] save). The sentinel can't use Vent again for 1d6 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Crafted from a nigh-indestructible metal of great rarity, adamant sentinels can't be destroyed except by the most powerful foes. Crafting an adamant sentinel requires a quantity of adamantine so massive that collecting it usually requires mounting a mining expedition to a distant planet, the Plane of Earth, or an Outer Plane.

```statblock
creature: "Adamant Sentinel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
