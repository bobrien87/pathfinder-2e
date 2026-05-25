---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Desert Giant"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +21, Intimidation +15, Survival +19, Desert Lore +18"
abilityMods: ["+6", "+6", "+5", "+3", "+4", "+0"]
abilities_top:
  - name: "Sandwalking"
    desc: "Desert giants have adapted to the loose sands of the desert and can move across them with ease. Desert giants ignore non-magical difficult terrain and uneven ground caused by sand."
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +21, **Will** +15"
health:
  - name: HP
    desc: "185"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +21 (`pf2:1`) (forceful, magical, reach 10 ft., sweep), **Damage** 2d6+12 slashing"
  - name: "Ranged strike"
    desc: "Rock +19 (`pf2:1`) (brutal, range 120 ft.), **Damage** 2d8+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sand Spin"
    desc: "`pf2:1` **Requirements** The desert giant is standing in sandy terrain <br>  <br> **Effect** The desert giant spins around and stirs up loose sand in a @Template[type:emanation|distance:10]. Until the beginning of the giant's next turn, creatures in the area are [[Concealed]], and other creatures are concealed to them."
  - name: "Scimitar Blitz"
    desc: "`pf2:2` The desert giant Strides up to their Speed, Striking once with each of their scimitars at any point during the movement."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Desert giants are nomadic humanoids who have dwelled in the world's most arid regions since time immemorial. Smaller peoples know that desert giants are the undisputed masters of desert living. Desert giants' strong cultural traditions play a large part in their ability to prosper in such harsh environs. Desert giant elders encourage their descendants to maintain abstemious lifestyles, particularly with regard to the consumption of food and drink. Most desert giants follow a simple vegetarian diet and maintain an incredible internal map of their home region's seasonal waterways and oases. Desert giants stand 15 feet tall, tending toward lean physiques that are ideal for traveling across vast expanses of sand for long sojourns.

Spread across the world, giants are as diverse as the isolated places they inhabit. A giant makes a big impression on the local environment, especially on smaller and weaker creatures.

```statblock
creature: "Desert Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
