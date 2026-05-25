---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Omox"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Ooze"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Chthonian, Draconic, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +23, Religion +20, Stealth +24"
abilityMods: ["+7", "+6", "+7", "+2", "+4", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Cleanly Vulnerability"
    desc: "An omox embodies filth, and they find the concept of cleanliness abhorrent. An omox subjected to an effect that cleans them, such as the tidy command of , takes 2d6 mental damage. They also take this damage the first time each round a creature hit by one of the omox's attacks spends actions cleaning off the filth."
  - name: "Slime Trap"
    desc: "A creature hit by an omox's slime ball must succeed at a DC 32 [[Reflex]] save or take a –10-foot circumstance penalty to its Speeds for 1 minute or until it Escapes. On a critical failure, the creature is also [[Clumsy]] 1 for the same duration. <br>  <br> > [!danger] Effect: Slime Trap"
armorclass:
  - name: AC
    desc: "25; **Fort** +23, **Ref** +21, **Will** +20"
health:
  - name: HP
    desc: "395; **Immunities** acid, critical hits, disease, poison, precision; **Weaknesses** cold iron 10, holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Absorb Weapon"
    desc: "`pf2:r` **Trigger** A creature hits the omox with a melee weapon <br>  <br> **Effect** The omox attempts to [[Disarm]] the creature. On a critical success, the weapon becomes subsumed within the omox's body rather than falling to the ground. Retrieving the weapon requires Disarming the omox of it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sludge Tendril +25 (`pf2:1`) (acid, unholy), **Damage** 2d6+13 bludgeoning plus 2d6 acid plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Slime Ball +23 (`pf2:1`) (acid, brutal, unholy, range 30 ft.), **Damage** 2d4+11 bludgeoning plus 2d6 acid plus [[Slime Trap]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24<br>**5th** [[Control Water]], [[Toxic Cloud]]<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**1st** [[Create Water]] (At Will)"
abilities_bot:
  - name: "Liquid Leap"
    desc: "`pf2:2` **Requirements** The omox is in a space of liquid. <br>  <br> **Effect** The omox teleports from its current space to any unoccupied space of liquid within 120 feet."
  - name: "Smother"
    desc: "`pf2:1` **Requirements** The omox has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The demon flows over the creature, covering it in oozing acidic slime. The creature must succeed at a DC 32 [[Fortitude]] save or it becomes [[Blinded]] and must hold its breath or begin suffocating. These effects lasts as long as the omox has the creature grabbed or restrained."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Seemingly made from living, animated filth, omoxes have no true anatomy, although they generally spend most of their time in roughly humanoid shapes, resembling some grim caricatures of half-melted humanoids. While scholars once believed these foul demons to be a pure, concentrated form of the corruption that suffuses the Outer Rifts and its inhabitants, in truth these demons arise from the souls of those who routinely befouled and polluted their surroundings in life.

When a sinful mortal soul is judged and sent on to the Outer Rifts, it can become a deadly fiend—a demon. Demons are living incarnations of sin—be they classic sins like wrath or gluttony, or more "specialized" depravities like an obsession with torture or the act of treason or treachery. Once formed, a demon's driving goals are twofold—the amassing of personal power, and the corruption of mortal souls to cause them to become tainted by sin. In this way demons ensure a never-ending supply of new demons to bolster their ever-growing ranks in the Outer Rifts.

Demons are selfish and self-absorbed creatures, and most firmly believe that mortals only play at being more virtuous than fiends. They enjoy tempting mortals into damnation to both indulge their egos and swell their armies. Like many other fiends, one of the great rewards of this manipulation is fulfilling their hunger for souls. In their eyes, the primary use for these souls is to spawn new demons, who can serve as soldiers, slaves, pawns, or even currency for their more powerful masters.

```statblock
creature: "Omox"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
