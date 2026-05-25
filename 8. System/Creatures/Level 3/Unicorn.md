---
type: creature
group: ["Beast", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Unicorn"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Fey"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +10, Diplomacy +11, Stealth +8, Survival +9"
abilityMods: ["+4", "+3", "+3", "+0", "+4", "+4"]
abilities_top:
  - name: "Animal Empathy"
    desc: "The unicorn has a connection to the creatures of the natural world that allows them to communicate with animals. They can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Ghost Touch"
    desc: "A unicorn's Strikes have the effects of a *[[Ghost Touch]]* property rune."
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "45; **Immunities** poison"
abilities_mid:
  - name: "+2 to Will Saves vs. Mental"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +12 (`pf2:1`) (holy, magical, unarmed), **Damage** 1d10+4 piercing plus 1d4 spirit"
  - name: "Melee strike"
    desc: "Hoof +12 (`pf2:1`) (agile, magical), **Damage** 1d8+4 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21, attack +13<br>**5th** [[Nature's Pathway]]<br>**2nd** [[Cleanse Affliction]]<br>**1st** [[Heal]], [[Light]]"
abilities_bot:
  - name: "Powerful Charge"
    desc: "`pf2:2` The unicorn Strides up to double its Speed in a straight line and then makes a horn Strike. If the unicorn moved at least 20 feet, it deals an additional 2d6 damage on a hit."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Symbols of grace and purity, unicorns resemble proud and noble horses. They typically have pure white coats, but they are best known for the single, delicate horn that extends from the center of their forehead. While unicorns often serve as protectors of unspoiled wilderness and sacred places, they are themselves highly sought after for their horns, which are said to possess potent magical properties. To many, the mere idea of hunting such a magnificent creature in the hopes of severing its horn is utterly reprehensible. Indeed, a dehorned unicorn is a sorry sight, and few such unicorns survive much longer in the wild.

Unicorns are found almost exclusively in remote, unsullied areas of wilderness. Sometimes associated with good-aligned deities, other times associated with nature and the fey, unicorns are always known for their righteousness and nobility. They are wary, at best, of most humanoid creatures, due in large part to poachers' tendency to hunt them for their horns, but unicorns are often rumored to have a weakness for those who are pure of both heart and spirit. Despite some tales, unicorns are equally likely to recognize purity in people of all genders.

```statblock
creature: "Unicorn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
