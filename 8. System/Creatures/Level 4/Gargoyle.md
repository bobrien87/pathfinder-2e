---
type: creature
group: ["Beast", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gargoyle"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Earth"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +9, Stealth +12"
abilityMods: ["+3", "+2", "+3", "-2", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +10, **Will** +10"
health:
  - name: HP
    desc: "40; **Immunities** bleed; **Resistances** physical 5 except adamantine"
abilities_mid:
  - name: "Clawed Feet"
    desc: "`pf2:r` **Trigger** The gargoyle is Flying, and a creature moves into an adjacent square below it. <br>  <br> **Effect** The gargoyle makes a claw Strike against the triggering creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (unarmed), **Damage** 2d8+3 piercing"
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, unarmed), **Damage** 2d6+3 slashing"
spellcasting: []
abilities_bot:
  - name: "Statue"
    desc: "`pf2:1` Until the next time it acts, the gargoyle appears to be a statue. It has an automatic result of 32 on Deception checks and DCs to pass as a statue."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gargoyles are monstrous hunters made of elemental stone. They use their resemblance to decorative statues to hide in plain sight in cities during the day and descend upon unlucky pedestrians at night. Their most common form is that of a horned humanoid with bat-like wings, but individual gargoyles show a great deal of variation, with some appearing more or less humanoid and others resembling no known creature. A gargoyle's features are not fixed; city-dwelling gargoyles who remain in the same locale long enough slowly morph, day by day, to match the style of the local architecture. These patient monsters can stay disguised for long stretches of time as they patiently await an opportunity to strike.

Gargoyles tend to be lone hunters, though sometimes they band into fearsome groups called wings for protection or sport. On rare occasions, wings become relatively stable communities, and gargoyles in wings may even ally with other creatures such as demons and intelligent aberrations, though these alliances exist on a razor's edge. The majority of gargoyles are treacherous, vindictive, and petty—traits that preclude lasting partnerships. Almost all have some subject they spend days mulling over while in statue form. Some are collectors, focusing on anything from books to grim trophies, while others are ritualistic or overly passionate about niche intellectual subjects or certain artistic motifs. These tendencies often contribute to the dissolution of wings as individuals with conflicting focuses clash.

Sanctified Roosts
In addition to their appearances matching their environment, gargoyles that position themselves on temples or other consecrated ground slowly succumb to the influence of that location. These gargoyles gain the holy or unholy trait, as do their unarmed Strikes. A gargoyle roosting on a temple of Asmodeus, for example, will eventually gain the unholy trait along with changes to their personality that bring it more in line with the god's ethos. Holy gargoyles are also possible, although gargoyles at such locations often abandon their roosts as their changing personality conflicts with their need to hunt.

```statblock
creature: "Gargoyle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
