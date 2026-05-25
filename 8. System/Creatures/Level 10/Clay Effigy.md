---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Clay Effigy"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +24"
abilityMods: ["+6", "-1", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Sacred Art"
    desc: "The creator of a clay effigy can dedicate the effigy to a deity while constructing it. If the deity allows a divine sanctification, the effigy is sanctified to that deity, gaining the holy or unholy trait as appropriate."
armorclass:
  - name: AC
    desc: "29; **Fort** +23, **Ref** +16, **Will** +17"
health:
  - name: HP
    desc: "175; **Resistances** physical 10 except adamantine, spells 10 except cold, earth, water"
abilities_mid:
  - name: "Effigy's Curse"
    desc: "When a creature damages the clay effigy, it must succeed at a DC 27 [[Will]] save or be afflicted with the effigy's curse. The accursed becomes [[Fatigued]] when it carries part of the effigy or any item the effigy was assigned to guard. <br>  <br> This fatigue can't be removed until the creature has given up such items for at least 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (magical, reach 10 ft., sanctified, unarmed), **Damage** 2d6 spirit plus 2d10+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Cast Out"
    desc: "`pf2:2` A @Template[emanation|distance:20] of spiritual energy pushes against intruders, as though trying to drive their souls away. Each creature in the area takes @Damage[8d6[spirit]|options:area-damage] damage depending on a DC 29 [[Will]] save. <br>  <br> The clay effigy can't Cast Out again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and 3d6 persistent,spirit damage. The persistent damage ends if the creature moves over 60 feet from the clay effigy or the effigy is destroyed. <br> - **Critical Failure** As failure, except the persistent damage is increased to 6d6 persistent,spirit."
  - name: "Heavy Stride"
    desc: "`pf2:2` The clay effigy Strides and can move through the spaces of Medium and smaller creatures. Each creature it moves through must succeed at a DC 29 [[Reflex]] save or be knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Traditionally, clay effigies are crafted in the image of a deity and used as guardians of tombs or sacred crypts. Clay effigies have the power to lay curses upon their victims as punishment for intrusion, leading many to believe that these oft-ancient constructs have a touch of the divine in them. Out of an abundance of caution, superstitious folk still tread lightly around elaborate or particularly well-crafted statues that resemble clay effigies even in the slightest.

For some clay effigies, this divine protection goes deeper. Even though deities rarely have the time to monitor their effigies, lesser divine servants are sometimes tasked with watching over an effigy. When the effigy is damaged, these guardians can sense it. The most precious effigies are layered with rituals that summon their guardians directly. Experienced tomb robbers learn to spot such markings from afar, so as to be forewarned of any divine interference in the area.

Although often assigned to protect valuable religious relics and other treasure, clay effigies' size and heavy movements make them ill-suited to stand guard among fragile items. Entire treasuries have been totally ruined by clumsy battles, so crafters do well to make sure their treasures are secured in sturdy containers—or otherwise place the effigy on the other side of the door from the treasures they wish to protect.

```statblock
creature: "Clay Effigy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
