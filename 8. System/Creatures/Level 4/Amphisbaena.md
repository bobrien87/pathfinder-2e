---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Amphisbaena"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +13, Stealth +12"
abilityMods: ["+5", "+4", "+2", "-4", "+0", "-4"]
abilities_top:
  - name: "Amphisbaena Venom"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d6 poison damage and [[Enfeebled]] 2 and [[Slowed]] 1 (1 round) <br>  <br> **Stage 3** 3d6 poison damage and [[Paralyzed]] (1 round)"
  - name: "Blinding Spittle"
    desc: "A creature critically hit by an amphisbaena's spit Strike is [[Blinded]] for 1 round."
armorclass:
  - name: AC
    desc: "21 all-around vision; **Fort** +10, **Ref** +14, **Will** +8"
health:
  - name: HP
    desc: "70; **Immunities** petrified"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +13 (`pf2:1`), **Damage** 2d6+5 piercing plus [[Amphisbaena Venom]]"
  - name: "Ranged strike"
    desc: "Spit +12 (`pf2:1`) (range 15 ft.), **Damage** 1d6 poison plus [[Amphisbaena Venom]] plus [[Blinding Spittle]]"
spellcasting: []
abilities_bot:
  - name: "Twin Bites"
    desc: "`pf2:1` An amphisbaena makes a fangs Strike with each of its heads, each against a different target. Both Strikes count toward its multiple attack penalty, but the penalty doesn't increase until after it has made both attacks."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An amphisbaena is an exceedingly aggressive, venomous viper of remarkable size that bears two heads-one on each end of its body. It moves in a manner similar to that of the more common sidewinder snake, throwing its body forward in a loop and anchoring itself by keeping one head or the other on the ground at all times.

Amphisbaenas' typical prey includes rabbits, foxes, various birds, small deer, and even humanoids if presented the opportunity. Fiercely territorial by nature, they attack just about anything that gets near their lairs, regardless of the intruder's size. Many a child has been warned about going too far into the woods alone, lest they wander too close to an amphisbaena den and become the creature's next meal.

The venom of an amphisbaena is incredibly potent, able to take down a stout dwarf within minutes if left untreated. However, it also has uses in a variety of healing remedies, which makes it a valuable commodity if collected. For example, a pregnant person might be advised to drink the venom in small, dilute doses to help safeguard the pregnancy. Mixing small amounts of the venom with various herbs and oil creates a poultice which dulls aches and pains. As a result, the image of an amphisbaena appears in many contexts associated with healing and alchemical subjects, such as labels for tinctures, annotations in herbalists' records, and illustrations in textbooks of medicine.

The first amphisbaena is said to have formed from the blood that fell as a medusa's head was severed. This story's origin most likely stems from the fact that amphisbaenas are oddly immune to petrification, which in turn leads to them sometimes being kept as pets by a medusa. A medusa who keeps an amphisbaena as a pet might regard the viper as their most treasured companion or perhaps even as their own child. Despite these fabled supernatural origins and the occasional special treatment they receive, however, amphisbaenas are entirely mundane animals with only rudimentary intelligence and no innate magical abilities whatsoever.

```statblock
creature: "Amphisbaena"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
