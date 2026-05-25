---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Witchwyrd"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Common, Draconic (One or more planar languages, Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +16, Athletics +15, Deception +15, Diplomacy +15, Intimidation +15, Desert Lore +14, one or more Lore skills related to a specific plane +0"
abilityMods: ["+3", "+3", "+1", "+4", "+3", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "22; **Fort** +13, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "110; **Resistances** force 5"
abilities_mid:
  - name: "Absorb Force"
    desc: "`pf2:r` **Frequency** once per round <br>  <br> **Trigger** A force barrage or Force Dart (see below) is fired at the witchwyrd, and the witchwyrd is aware of it and has a free hand <br>  <br> **Effect** The witchwyrd \"catches\" one force projectile, absorbing it, preventing the damage, and causing that hand to glow while it holds this energy. A hand that's holding energy can't be used for any other purpose except to use Force Dart. The energy lasts for 1 minute or until it's released."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+6 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Ranseur +16 (`pf2:1`) (disarm, magical, reach 10 ft.), **Damage** 1d10+6 piercing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 23, attack +15<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]], [[Translocate]]<br>**2nd** [[Blur]], [[Dispel Magic]], [[Resist Energy]]<br>**1st** [[Carryall]] (At Will), [[Detect Magic]], [[Phantasmal Minion]] (At Will)"
abilities_bot:
  - name: "Force Dart"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> The witchwyrd fires one dart of force per action spent (dealing @Damage[(1d4+1)[force]] damage each). They can't spend more actions on this ability than they have free hands. If they use a hand that has Absorbed Force, that hand hurls two darts instead of one, expending the held energy."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Witchwyrds conceal most of their faces, leaving only their eyes unmasked. Their inscrutability is a boon to one of their most significant interests—mercantilism—and many haughty witchwyrds openly revel in the befuddlement inspired by their mysterious guises and mannerisms. Witchwyrds have a keen eye for new opportunities and markets, and they almost always know when someone tries to pull one over on them.

These four-armed humanoid creatures have hairless blue-gray skin, are typically 6-1/2 feet tall, and weigh 300 pounds. Their hands have three evenly sized and spaced digits in a tripod-like arrangement. When not trying to blend in with the local community, witchwyrds favor outlandish, loose-fitting clothes in bright reds or yellows and a signature conical hat. They tend to prefer the driest, warmest regions of the lands they visit—perhaps an indicator of their mysterious home world. Witchwyrds are notoriously closemouthed about details of this distant place, and with good reason: most witchwyrds on Golarion have never visited their ancestral home. To these witchwyrds, the notion of a home planet is a constant thorn in their side, and when asked, many choose to ignore the question altogether. Others are so agitated by these queries that they respond with impatience or even violence. Some scholars have theorized a connection between witchwyrds and several other four-armed creatures, but as with questions of their place of origin, witchwyrds have little to say about the topic.

```statblock
creature: "Witchwyrd"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
