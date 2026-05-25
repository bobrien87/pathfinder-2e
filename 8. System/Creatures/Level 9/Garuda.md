---
type: creature
group: ["Celestial", "Holy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Garuda"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Celestial"
trait_02: "Holy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Common, Empyrean, Vudrani (Plus two others, Speaker of the skies)"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +21, Diplomacy +19, Intimidation +17, Religion +19"
abilityMods: ["+6", "+4", "+4", "+2", "+4", "+4"]
abilities_top:
  - name: "Speaker of the Skies"
    desc: "A garuda can speak with any type of bird."
  - name: "Vehicle of the Gods"
    desc: "Garudas were created to serve as transport for other beings. A holy creature can ride the garuda by using the [[Mount]] action to move onto them. Unlike the normal rules for riding other creatures, both the garuda and the rider continue to receive all 3 of their actions each turn, and the garuda's rider can be Medium or smaller. A garuda can have only a single rider at a time. The garuda can choose to allow a non-holy (but not an unholy) creature to ride them, but generally only does so in specific circumstances."
  - name: "Divine Grasp"
    desc: "When a garuda moves, they can bring grabbed creatures along with them."
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +19, **Will** +16"
health:
  - name: HP
    desc: "160; **Weaknesses** unholy 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +21 (`pf2:1`) (holy, magical), **Damage** 2d10+9 piercing plus 1d6 fire"
  - name: "Melee strike"
    desc: "Talon +21 (`pf2:1`) (agile, finesse, holy, magical), **Damage** 2d8+9 bludgeoning plus 1d6 fire plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Sun Beam +19 (`pf2:1`) (fire, holy, magical), **Damage** 2d10 fire plus 2d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +18<br>**4th** [[Translocate]]<br>**3rd** [[Haste]], [[Holy Light]]<br>**2nd** [[Blazing Bolt]]"
abilities_bot:
  - name: "Celestial Meteor"
    desc: "`pf2:3` **Requirements** The garuda doesn't have a rider <br>  <br> **Effect** The garuda Flies straight up and then comes crashing down toward the ground, landing in an unoccupied space within 30 feet. As the garuda lands, a burst of solar flames erupts from them, dealing @Damage[5d6[fire]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:10] (DC 28 [[Reflex]] save). If the garuda lands adjacent to a creature, they can attempt to [[Grapple]] that creature. On a success or critical success, the garuda can then Fly up to 30 feet with the creature."
  - name: "Raise by the Sun"
    desc: "`pf2:2` `pf2:2` to `pf2:3` <br>  <br> **Requirements** The garuda doesn't have a rider <br>  <br> **Effect** The garuda Flies and picks up a willing creature at any point during the flight, who then begins riding the garuda, and then the garuda continues their Fly action. If the garuda uses three actions, they can instead Fly twice. At any point during the garuda's movement, the rider can use a reaction to attempt a Strike with a ranged weapon."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Garudas are winged humanoids created to serve holy gods and other powerful celestial beings. Originally born among the celestial planes, garudas eventually spread beyond, with many making their way to the mortal Universe. As divine servants, garudas' primary roles are as protectors, defending holy sites and important divine figures like high priests.

The most important role a garuda serves is as a means of transportation. The first garudas served as mounts for the gods, carrying them across the heavens and into combat. This tradition continues today, with garudas willingly serving as mounts for champions, clerics, and other divine chosen. On occasion, a god will request a garuda track down one of the god's followers. The garuda declares their servitude to the follower, acting as a guardian and transport for as long as the god decrees.

```statblock
creature: "Garuda"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
