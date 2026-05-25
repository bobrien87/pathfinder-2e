---
type: creature
group: ["Humanoid", "Titan"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Thanatotic Titan"
level: "22"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Titan"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Common, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +45, Crafting +41, Deception +36, Intimidation +38, Religion +38, Stealth +36"
abilityMods: ["+10", "+4", "+9", "+8", "+6", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Void Explosion"
    desc: "If the titan's void chunk Strike isn't a critical failure, the chunk explodes, dealing @Damage[10d6[void]|options:area-damage] damage to all creatures in a @Template[type:burst|distance:20] (DC 45 [[Reflex]] save)."
armorclass:
  - name: AC
    desc: "46; **Fort** +37, **Ref** +34, **Will** +35"
health:
  - name: HP
    desc: "540; **Immunities** death effects, disease"
abilities_mid:
  - name: "+4 Status to All Saves vs. Mental or Divine"
    desc: ""
  - name: "Impossible Stature"
    desc: "100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 47 [[Will]] save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "`pf2:r` The titan can use their Reactive Strike when a creature within their reach uses a concentrate action, in additional to its normal trigger. They disrupt actions on any hit, not just a critical hit—including triggering concentrate actions. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Godslayer"
    desc: "`pf2:0` **Trigger** The titan damages a creature capable of using divine spells or abilities <br>  <br> **Effect** The creature must attempt a DC 45 [[Will]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature can't use divine spells or abilities for 1 round and is [[Frightened]] 2. Only powerful non-divine magic, such as manifestation, can undo this effect. <br> - **Failure** As success, but the duration is 1 minute. <br> - **Critical Failure** As success, but the duration is unlimited."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Halberd +42 (`pf2:1`) (magical, reach 40 ft., versatile s), **Damage** 4d10+25 piercing"
  - name: "Melee strike"
    desc: "Foot +39 (`pf2:1`) (agile, reach 30 ft.), **Damage** 4d8+20 bludgeoning"
  - name: "Ranged strike"
    desc: "Void Chunk +39 (`pf2:1`) (brutal, void, range 200 ft.), **Damage** 3d12 bludgeoning plus 2d10 void plus [[Void Explosion]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 45, attack +37<br>**9th** [[Falling Stars]], [[Massacre]]<br>**8th** [[Spiritual Epidemic]] (At Will)<br>**7th** [[Spell Riposte]]<br>**6th** [[Scrying]], [[Truesight]] (Constant)<br>**5th** [[Sending]]<br>**4th** [[Suggestion]] (At Will)<br>**2nd** [[Dispel Magic]] (At Will)"
abilities_bot:
  - name: "Titanic Charge"
    desc: "`pf2:2` The titan Strides twice and makes a melee Strike. If the Strike hits, the titan can cast [[Earthquake]] centered on the target as a free action."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 45 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Wide Cleave"
    desc: "`pf2:2` The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Thanatotic titans served as assassins in the war against the deities. They learned to sever their targets' divine connections, murdering mortal priests and divine heralds alike. Thanatotic titans were locked away in the Outer Rifts, but some have freed themselves and crept out from the Outer Rifts so they might continue their sprees of murder and mayhem. They maintain a devotion to their purpose and a grudge, and to this day, they seek out the faithful for slaughter.

Created by ancient deities long before the rise of mortal ancestries, titans united and attempted to overthrow their deific progenitors. The resulting war still figures prominently throughout mortal myths, in which most titans were cast down and imprisoned for eons.

```statblock
creature: "Thanatotic Titan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
