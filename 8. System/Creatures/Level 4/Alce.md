---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Alce"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +12, Intimidation +10, Stealth +11, Survival +9"
abilityMods: ["+4", "+3", "+3", "-4", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +13, **Will** +7"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +14 (`pf2:1`) (deadly d10, unarmed), **Damage** 2d8+4 piercing"
  - name: "Melee strike"
    desc: "Talon +14 (`pf2:1`) (agile, unarmed), **Damage** 2d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The alce Strides and makes a talon Strike at the end of that movement. If the alce began this action [[Hidden]], it remains hidden until after the attack."
  - name: "Regal Shriek"
    desc: "`pf2:1` The alce unleashes a shriek that transitions into a terrifying roar. Each creature in a @Template[emanation|distance:60] must attempt a DC 20 [[Will]] save. Regardless of the result, creatures are temporarily immune to all griffons' Regal Shrieks for 10 minutes. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. Animals are [[Slowed]] 1 for as long as they're frightened. <br> - **Critical Failure** The creature is [[Frightened]] 3. Animals are [[Paralyzed]] as long as they're frightened."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wingless griffons, known as alces, result from a rare mutation. Among a clutch of winged griffons, the alce is typically considered the runt, so alces are rarely seen on their own in the wild, though they're often intentionally bred in captivity as relatively affordable exotic mounts.

Griffons are regal beasts revered as symbols of freedom and strength in many cultures. They are physically striking, with the hindquarters of a lion and the head, wings, and forelimbs of a great bird of prey—typically an eagle, but some instead bear the features of a hawk, falcon, or even an osprey or vulture. In rare cases, the griffon's hindquarters may resemble those of a different great cat, such as a leopard or tiger. The variations seem to conform to the griffon's environment—for instance, especially rare griffons of northern Avistan have the hindquarters of a Grungir lynx and the upper body of a snowy owl.

Wild griffons rely on their powerful wings to hold them aloft and their keen eyesight to spy out prey. The speed with which they plunge toward the ground and snatch up victims is astonishing. They often tear apart a kill's flesh with razor-sharp beaks but not before alighting to secluded location where they can enjoy their meal without interruption. Griffons hunting to feed their chicks are more cautious, tearing apart prey rather than risking bringing a living creature back to their nests.

Skilled animal trainers long ago learned how to raise griffons as mounts for military forces or powerful individuals. Such mounts are known for their strength, bravery, and unfailing loyalty. They are among the smartest of animals, and many griffon variants are considered intelligent beasts instead; it's thought that a griffon chooses its rider as much as a rider chooses the griffon. The process of training a griffon to accept and carry a rider in flight is a long and expensive ordeal. Griffon trainers charge rich sums for their services, and a ruler who can boast of owning a stable of griffons is the subject of great respect and envy.

```statblock
creature: "Alce"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
