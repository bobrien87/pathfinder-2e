---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dragon Turtle"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common, Draconic, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +21, Diplomacy +18, Intimidation +18, Stealth +13, Survival +17"
abilityMods: ["+6", "+0", "+4", "+1", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "29; **Fort** +19, **Ref** +15, **Will** +17"
health:
  - name: HP
    desc: "140; **Immunities** paralyzed, sleep"
abilities_mid:
  - name: "Shell Block"
    desc: "`pf2:r` **Trigger** A creature adjacent to the dragon turtle targets it with a melee attack. <br>  <br> **Effect** The dragon turtle rolls its shell toward the triggering creature, gaining a +2 circumstance bonus to its AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+9 piercing"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, unarmed), **Damage** 2d8+9 slashing"
spellcasting: []
abilities_bot:
  - name: "Capsize"
    desc: "`pf2:1` The dragon turtle tries to capsize an adjacent aquatic vessel of their size or smaller. The dragon turtle must succeed at a DC 30 [[Athletics]] check (reduce the DC by 5 for each size smaller than the dragon turtle) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Conjure Storm"
    desc: "`pf2:1` The dragon turtle summons a mighty storm to rage around themself. The area in a @Template[emanation|distance:30] around the turtle becomes difficult terrain for all other flying and swimming creatures. The dragon turtle can end the storm by taking this action again."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon turtle makes two Claw Strikes and one Jaws Strike in any order."
  - name: "Tsunami"
    desc: "`pf2:2` The dragon turtle unleashes their destructive prowess by creating a massive growing wave that deals @Damage[7d6[bludgeoning]|options:area-damage] damage in a @Template[cone|distance:60] (DC 27 [[Reflex]] save). The wave's damage increases by 10 for creatures who are more than 30 feet away. A creature that fails its save is knocked [[Prone]]. <br>  <br> The dragon turtle can't use Tsunami again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These immense aquatic dragons have rocky shells similar to those of tortoises and flippers powerful enough to overturn hardy vessels. The fearsome creatures enjoy being considered as dangerous as storms or natural disasters by seafaring folk. Despite their reputation, many dragon turtles delight in secretly observing seafaring cities grow and evolve throughout the ages. They have even been known to protect such cities from pirates, invading armies, or even other dangerous sea creatures. According to rumor, these turtles have even hired adventurers to handle more inland threats. Such cities will often offer tribute to the great turtle if they discover its intervention. While a dragon turtle hoards the treasures of the ships it sinks, they consider the bounty freely offered from their protected city most precious.

While many dragon turtles are already large enough to inspire awe, some can grow substantially larger. Those massive, ancient dragon turtles are somnolent, resembling rocky islands from a distance; their prodigious hoards can be a source of ancient sea lore. Legends persist of truly immense dragon turtles who spend centuries drifting on the surface of the ocean, far from established shipping lanes or charted waters, with shells that serve as islands capable of supporting entire ecosystems and even, some claim, small settlements whose inhabitants know nothing of land that doesn't drift across the sea.

```statblock
creature: "Dragon Turtle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
