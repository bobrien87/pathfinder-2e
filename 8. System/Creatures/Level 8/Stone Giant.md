---
type: creature
group: ["Earth", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stone Giant"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common, Jotun, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +20, Intimidation +14, Nature +18, Stealth +14"
abilityMods: ["+6", "+2", "+4", "+0", "+4", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +14, **Will** +14"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "Swat Projectile"
    desc: "`pf2:r` **Requirements** The stone giant must have a free hand but can Release anything as part of this reaction <br>  <br> **Trigger** The giant is targeted by a physical ranged attack <br>  <br> **Effect** The stone giant gains a +4 circumstance bonus to AC against the triggering attack. If the attack misses and the projectile was made of stone, the giant can throw it back at the attacker as a rock ranged Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +21 (`pf2:1`) (backswing, magical, reach 10 ft., shove), **Damage** 2d10+12 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d6+14 bludgeoning"
  - name: "Ranged strike"
    desc: "Rock +18 (`pf2:1`) (brutal, range 120 ft.), **Damage** 2d6+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Big Swing"
    desc: "`pf2:2` The stone giant makes a greatclub Strike. The target is Pushed up to 10 feet on a hit or up to 20 feet on a critical hit. <br>  <br> If the target collides with a solid object, it takes bludgeoning damage as though it had fallen the distance it moved."
  - name: "Create Boulder"
    desc: "`pf2:1` The stone giant molds a boulder from primal earth and throws it as a rock Strike. A creature hit by the Strike must succeed at a DC 26 [[Reflex]] save or be knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Stone giants are stoic, reclusive herders and artists with a rich history and collection of traditions. They dwell in caves in tall mountains and craggy ranges, where their grayish skin allows them to blend in with their surroundings and go unnoticed, despite being around 12 feet tall. Benign travelers who come across a clan of stone giants need not worry, however, for stone giants do not actively invite confrontation or strife. They are, by and large, peaceful people who seek wisdom through exploration of nature and long meditations on the elements of the natural world. Their elders are among the wisest of giants, using their charisma and druidic magic to lead their clans to prosperity and harmony with nature.

A stone giant clan will usually raise a number of animals as pets, favoring cave bears, elephants, or dinosaurs depending on the environment. Many clans also accept allies, considering arboreals, elementals, and even gargoyles as kin through their shared connection with the earth.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Stone Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
