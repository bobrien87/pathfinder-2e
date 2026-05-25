---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shriezyx"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +12"
abilityMods: ["+3", "+5", "+4", "-4", "+2", "+0"]
abilities_top:
  - name: "Numbing Toxin"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** 1d8 poison damage, clumsy 2, and [[Slowed]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "70; **Weaknesses** fire 6; **Resistances** poison 6"
abilities_mid:
  - name: "+1 Status to All Saves vs. Mental"
    desc: ""
  - name: "Pyrophobia"
    desc: "If the shriezyx takes fire damage or starts its turn within 30 feet of a fire at least the size of a torch, it becomes [[Frightened]] 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +13 (`pf2:1`) (finesse), **Damage** 2d6+5 piercing plus [[Numbing Toxin]]"
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, finesse), **Damage** 2d4+5 slashing"
spellcasting: []
abilities_bot:
  - name: "Clicking Scurry"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The shriezyx Strides or Climbs, and then makes a claw Strike."
  - name: "Flash Web"
    desc: "`pf2:2` The shriezyx's shoots a fleshy web at a target within 30 feet. The target must succeed at a DC 20 [[Reflex]] save or become [[Immobilized]] and exposed to numbing toxin. Due to the grotesque nature of the webbing, the target becomes [[Sickened]] 1 and can't reduce its sickened condition until it Escapes (DC 20)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Long ago, Thassilonian wizards created shriezyx in twisted experiments to act as guards and test subjects. These 300-pound aberrations have outlived their creators and mostly make their homes inside Thassilonian ruins, caverns, and deep in the Darklands. Their bodies are covered in hard, extremely flammable chitin that molts as they grow.

While a shriezyx looks like a bestial, three-eyed spider, the truth behind these creatures is far more grotesque. Instead of spinning silk, a shriezyx spits strands of unformed, sticky flesh from its mouth. When fresh, theses fleshy strands are coated in a nerve-numbing toxin that slows prey. The weblike flesh-spittle coats shriezyx lairs and nests, wrapped around the bones for their former meals. Fortunately for those who stumble into these lairs, a shriezyx's toxin dissipates when exposed to air, leaving the fleshy webs only sickeningly sticky. Unfortunately for those same travelers, shriezyx are often communal creatures that gather in large numbers and are quick to attack intruders.

Deros and other subterranean peoples sometimes keep shriezyx as guards or mounts, using food and threats of fire to keep them in line. Most shriezyx owners are quick to dispose of any eggs, fearing a swarm could grow beyond their control, but some breeders have realized that a shriezyx's offspring retain much of its parent's demeanor and save the eggs of the most loyal (or most fire-fearing) shriezyx in hopes of creating a profitable, easier-to-control herd. While crueler masters might use shriezyx as test subjects, alchemists often see these creatures as beloved pets. Their grotesque webs make great alchemical reagents and provide ethically sourced flesh for experiments, while the molted exoskeleton can be used to create bombs and other explosives.

```statblock
creature: "Shriezyx"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
