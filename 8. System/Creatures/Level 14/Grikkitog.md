---
type: creature
group: ["Aberration", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grikkitog"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aberration"
trait_02: "Earth"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +28, Deception +27, Survival +25"
abilityMods: ["+8", "+4", "+5", "+2", "+5", "+5"]
abilities_top:
  - name: "Manifold Vision"
    desc: "While its core is implanted, the grikkitog can see through the eyes it creates throughout the area of its infestation aura, gaining the benefits of [[All Around Vision]]."
  - name: "Earth Glide"
    desc: "The grikkitog can Burrow through dirt and stone at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "36; **Fort** +28, **Ref** +23, **Will** +24"
health:
  - name: HP
    desc: "200; **Resistances** all damage 10 except adamantine"
abilities_mid:
  - name: "Infestation Aura"
    desc: "120 feet. <br>  <br> While its core is implanted, a grikkitog infests all earth and stone within 120 feet, as long as there is a contiguous physical connection between the earth, including stone objects touching the ground. This effect spreads even if the grikkitog does not have line of effect, though it can affect earth or stone on the surface and exposed to the air only if at least part of its core is exposed as well. <br>  <br> Within the aura, it can grow maws and eyes everywhere. It can make jaws attacks against any creature, originating from any earth or stone in the aura adjacent to that creature. Determine cover from the origin point of the attack, not from the grikkitog's core."
  - name: "Barbed Maw"
    desc: "`pf2:0` **Trigger** The grikkitog hits a creature with a jaws Strike <br>  <br> **Effect** The grikkitog sinks its barbed teeth into the target, which must succeed at a DC 34 [[Reflex]] save or be [[Immobilized]]. While immobilized, the victim takes 3d8 persistent,bleed damage and the grikkitog feeds upon its flesh. The creature is immobilized until the grikkitog ends the effect as a free action or the target succeeds at a DC 38 check to `act escape dc=38`. <br>  <br> The grikkitog can immobilize any number of creatures with these maws."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +29 (`pf2:1`) (magical, unarmed), **Damage** 3d12+14 piercing plus [[Barbed Maw]]"
spellcasting: []
abilities_bot:
  - name: "Implant Core"
    desc: "`pf2:3` The grikkitog implants its core into an adjacent section of earth or stone, melding seamlessly and changing its visual appearance to match the surrounding rock. It's [[Immobilized]] but automatically succeeds at its Deception check to Impersonate the stone around it; creatures actively searching for it can still attempt Perception checks against its Deception DC as normal. A grikkitog can release its implantation as a free action, which has the manipulate trait. A grikkitog's infestation aura and manifold vision are only active while implanted."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Grikkitogs, also known as the "hungry earth," are strange parasites from the Plane of Earth that infest earth, rock, and stone in order to feed their endless hunger. A young grikkitog is a formless apparition until it corrupts an earth elemental host, forming the grikkitog's core. A grikkitog can then possess the earth and stone nearby with its voracious essence, forming maws and eyes all around it. These creatures can be particularly dangerous to small creatures that lair within gaps among rocks, as well as mountain climbers searching for the perfect handhold.

```statblock
creature: "Grikkitog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
