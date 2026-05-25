---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ganzi Martial Artist"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Common, Protean"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +10, Deception +7, Performance +7, Stealth +9"
abilityMods: ["+3", "+4", "+0", "-1", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +7, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "36"
abilities_mid:
  - name: "+1 Status to All Saves vs. Controlled Condition"
    desc: ""
  - name: "Ganzi Resistance"
    desc: "The ganzi gains resistance 1 to acid, electricity, or sonic (chosen randomly each day). <br>  <br> > [!danger] Effect: Ganzi Resistance"
  - name: "Ganzi Spells"
    desc: "Two of the following chosen at random each day using 1d12 <br>  <br> - [[Acid Grip]] <br> - [[Blur]] <br> - [[Humanoid Form]] <br> - [[Illusory Object]] <br> - [[Invisibility]] <br> - [[Laughing Fit]] <br> - [[Noise Blast]] <br> - [[Paranoia]] <br> - [[Resist Energy]] <br> - [[See the Unseen]] <br> - [[Shatter]] <br> - [[Telekinetic Maneuver]]"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shuriken +11 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Foot +11 (`pf2:1`) (agile, finesse, sweep), **Damage** 1d8+5 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells (See Ganzi Spells)"
    desc: "DC 19, attack +11<br>**2nd** [[Acid Grip]], [[Blur]], [[Humanoid Form]], [[Invisibility]], [[Laughing Fit]], [[Noise Blast]], [[Paranoia]], [[Resist Energy]], [[See the Unseen]], [[Shatter]], [[Telekinetic Maneuver]]<br>**1st** [[Illusory Object]]"
abilities_bot:
  - name: "Flurry of Kicks"
    desc: "`pf2:1` **Frequency** once per turn <br>  <br> **Effect** The martial artist makes two melee Strikes. The martial artist applies their multiple attack penalty to these Strikes normally."
  - name: "Handspring Kick"
    desc: "`pf2:1` **Requirements** The martial artist has both hands free <br>  <br> **Effect** The martial artist Steps, then makes a melee Strike at a –1 penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Children of primeval chaos, ganzis intertwine the churning pandemonium of the Maelstrom with the more mundane tumult of mortal life. Some arise in bloodlines touched by creatures of the Maelstrom in generations previous, while others are changed by planar friction seething upon the shores of creation, but all share the essence of anarchy in their blood and bone.

Due to their connection to the Maelstrom, ganzis vary wildly in appearance; the most common proteankin have patches of scales and feathers and mischievous, slithering tails. Others might have stranger features, such as horns, glowing orange eyes, or limbs flickering with harmless auras of entropic energy. Ganzis might be dramatically shorter, taller, thinner, or stouter than is typical for their ancestry, and it's not uncommon for them to be mistaken for more common nephilim.

Independent-minded to a fault, often creative and capricious, ganzis prefer professions that allow them to serve as their own masters. If such a profession gives a ganzi opportunity to baffle or befuddle Golarion's more staid citizens, then all the better. Ganzis frequently develop reputations as outgoing, deviant, or thrill-seeking, and many heartily embrace these reputations and lean into them. Of all the planar scions, ganzis are among the most likely to take up life as wanderers.

Ganzis with a taste for close combat are sometimes drawn to martial arts, turning their curious forms into potent and unexpected weapons. It's common to find such ganzi in the temporary employ of others, whether out of a legitimately shared ideology or simply the need for money. Just as often, though, one can simply find a ganzi martial artist demonstrating their craft on a street corner or dealing out justice to enforcers of cruel laws.

Nephilim are individuals infused with the essence of an immortal being from the Outer Planes, such as a celestial, fiend, or monitor. While the examples presented here are humans with nephilim heritages that trace back to Axis and the Maelstrom, members of nearly any ancestry can be born with an influx of similar energies and become a planar scion. More about nephilim can be found starting on page 78 of Player Core, and other nephilim NPCs are presented beginning on page 266 of Monster Core.

```statblock
creature: "Ganzi Martial Artist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
