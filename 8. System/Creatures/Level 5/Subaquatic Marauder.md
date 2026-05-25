---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Subaquatic Marauder"
level: "5"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Crafting +13, Ocean Lore +12"
abilityMods: ["+4", "+2", "+4", "+2", "+1", "+0"]
abilities_top:
  - name: "Sealed Diving Suit"
    desc: "The marauder's diving suit is a technological marvel. When sealed, it provides 1 hour of fresh air and protects the wearer from exposure to inhaled threats. Personalized modifications and a need for constant tinkering mean that other creatures are unable to take advantage of the special abilities of the diving suit and treat it as an ordinary suit of half plate."
armorclass:
  - name: AC
    desc: "23; **Fort** +15, **Ref** +7, **Will** +12"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gauntlet +15 (`pf2:1`) (agile, free hand), **Damage** 1d4+8 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +15 (`pf2:1`) (tethered, thrown 30), **Damage** 1d6+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Depth Charge"
    desc: "`pf2:2` The marauder pulls a release valve on their suit, expelling a pressure wave that deals @Damage[3d6[sonic],3d6[bludgeoning]|options:area-damage] damage (DC 22 [[Fortitude]] save) to all creatures in a @Template[type:emanation|distance:10]. Creatures that fail the save take a –2 circumstance penalty to Acrobatics checks to [[Balance]] and Athletics checks to [[Swim]] for 1 minute as their inner ear is impaired. Creatures that critically fail the save are also [[Deafened]] for 1 minute. The marauder can't use Depth Charge again for 1d4 rounds. <br>  <br> > [!danger] Effect: Depth Charge"
  - name: "Retract"
    desc: "`pf2:1` **Requirements** The marauder's last action was a successful javelin strike <br>  <br> **Effect** The marauder reels in a chain connected to the javelin, pulling the target up to 10 feet closer. They then Interact to return the javelin to their hand."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A new breed of pirate, these raiders strike at unsuspecting ships from beneath the cover of the waves. The bulky, reinforced diving suits they wear also serve as armor and clockwork mechanisms augment their strength.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Subaquatic Marauder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
