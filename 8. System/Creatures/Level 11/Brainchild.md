---
type: creature
group: ["Illusion", "Mental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Brainchild"
level: "11"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Illusion"
trait_02: "Mental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "telepathy 100 feet, universal language"
skills:
  - name: Skills
    desc: "Deception +22, Intimidation +24, Performance +22, Society +21, Stealth +20"
abilityMods: ["+4", "+5", "+4", "+2", "+3", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Universal Language"
    desc: "Anything spoken by the brainchild is perceived by the listener in its native language."
  - name: "Urban Legend"
    desc: "A brainchild is sustained only by the reputation that precedes them. Mindless creatures are immune to a brainchild and can't perceive them. <br>  <br> The brainchild's size, features, and items, as well as the appearance of their attacks, match what the foes perceiving them expect. If foes expect to see different things, the brainchild chooses which to manifest. If any creature that can perceive the brainchild believes the brainchild has one of the abilities below, the brainchild has that ability. <br>  <br> A creature can [[Seek]] or [[Sense Motive]] (against the brainchild's Deception DC) to attempt to disbelieve an individual ability. If at any point no creature perceiving the brainchild believes in the ability, the brainchild loses that ability immediately. If foes expect different particulars, such as one believing the brainchild is immune to fire and another believing they're immune to divinations, the brainchild chooses one to have. <br>  <br> - **[[Tremorsense]]** (imprecise) 100 feet <br>  <br> - **Immunity** to one damage type, magic school, or condition <br>  <br> - **Weakness** 10 to one damage type other than mental <br>  <br> - **Resistance** 10 to physical damage, with an exception for either cold iron or silver <br>  <br> - **[[Frightful Presence]]** (aura, emotion, fear, mental) 100 feet, DC 28 <br>  <br> - **1d6 Extra Damage** on Strikes, of a type one foe believes in <br>  <br> - **Additional Spells** [[Phantom Pain]] and [[Shadow Blast]] at 6th rank"
armorclass:
  - name: AC
    desc: "30; **Fort** +21, **Ref** +22, **Will** +18"
health:
  - name: HP
    desc: "200; **Immunities** death effects, disease, doomed, scrying; **Weaknesses** mental 10"
abilities_mid:
  - name: "Persistence of Memory"
    desc: "When a brainchild is destroyed, it returns if anyone still fully believes it exists, re-forming within 100 feet of any believer after 2d4 days."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Illusory Weapon +24 (`pf2:1`) (illusion, mental, occult), **Damage** 4d6+10 mental plus [[Urban Legend]]"
  - name: "Ranged strike"
    desc: "Illusory Weapon +24 (`pf2:1`) (illusion, mental, occult), **Damage** 4d6+6 mental plus [[Urban Legend]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22<br>**4th** [[Translocate]], [[Vision of Death (image resembles the brainchild)]]<br>**1st** [[Figment]], [[Message]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A rumor can become so vivid and persistent that it comes to life, creating a brainchild—a living illusion that hatches from an intense belief in a remorseless and implacable killer. Often, these rumors are borne from victims of a [[Vision of Death]] spell. A brainchild's capabilities grow when they pursue a believer but deflate against skeptics, making them only as dangerous as one believes them to be. A simple drive to stalk, terrify, and kill propels a brainchild, but the creature might also exhibit other behaviors ascribed to them through gossip.

```statblock
creature: "Brainchild"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
