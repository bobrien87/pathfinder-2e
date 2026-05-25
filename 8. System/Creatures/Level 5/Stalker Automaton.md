---
type: creature
group: ["Automaton", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stalker Automaton"
level: "5"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Automaton"
trait_02: "Construct"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common (One other language the stalker knew in life usually jistkan, Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +11, Stealth +14, Survival +13"
abilityMods: ["+4", "+5", "+3", "+3", "+4", "+1"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Sneak Attack"
    desc: "The creature's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "65; **Resistances** physical 5 except adamantine"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`), **Damage** 2d10+6 piercing"
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (agile), **Damage** 2d6+6 slashing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 20, attack +0<br>**4th** [[Translocate]] (At Will)"
abilities_bot:
  - name: "Astral Blink"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The stalker steps sideways into the astral realm, reappearing nearby. The stalker teleports to an unoccupied space within 15 feet that they can see."
  - name: "Astral Pounce"
    desc: "`pf2:2` **Requirements** The stalker hasn't used Astral Blink this round <br>  <br> **Effect** The stalker Astral Blinks or Strides and makes a Strike at the end of that movement. If the stalker began this action [[Hidden]], it remains hidden until after this ability's Strike. The stalker then Astral Blinks or Strides again, whichever it did not already do."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Stalker automatons house the minds of skilled hunters, scouts, and assassins in bodies patterned after the great hunters of the natural world. Stalkers generally have the shape of wolves, large cats, and other predatory creatures. The ancient artifcers improved upon their natural abilities, adding in specialized systems of arcane camoufage and movement. Surviving stalkers still pride themselves as hunters without peer, even as they've adapted to their animalistic forms.

```statblock
creature: "Stalker Automaton"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
