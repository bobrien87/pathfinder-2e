---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Brimorak"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Chthonian, Draconic, Empyrean, Pyric (Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Deception +11, Religion +10, Stealth +12"
abilityMods: ["+4", "+3", "+4", "+1", "+1", "+2"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Extinguishing Aversion"
    desc: "Dousing a brimorak with water, either ordinary water or from a water effect, causes no physical harm to the fiend but deals 3d6 mental damage. Fully immersing the brimorak in water deals 5d6 mental damage per round."
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a brimorak's vision; they ignore the [[Concealed]] condition from smoke."
  - name: "Flaming Weapon"
    desc: "A brimorak's hooves and any weapon they wield burst into flame. They can also Interact to create a sword of fire and steel, which dissolves if it leaves their grip."
armorclass:
  - name: AC
    desc: "22; **Fort** +15, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "80; **Immunities** fire; **Weaknesses** cold iron 5, holy 5"
abilities_mid:
  - name: "Boiling Blood"
    desc: "Each time an adjacent creature deals slashing or piercing damage to the brimorak, the attacker is sprayed with the brimorak's boiling blood, which deals 2d4 fire damage (DC 19 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flaming Sword +15 (`pf2:1`) (magical, unholy), **Damage** 2d8+4 slashing plus 1d6 fire"
  - name: "Melee strike"
    desc: "Hoof +15 (`pf2:1`) (agile, unholy), **Damage** 2d4+4 bludgeoning plus 1d6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**4th** [[Translocate]]<br>**3rd** [[Fireball]]<br>**2nd** [[Dispel Magic]]<br>**1st** [[Ignition]]"
abilities_bot:
  - name: "Frothing Spew"
    desc: "`pf2:2` The brimorak spits their boiling blood in a @Template[line|distance:20] that deals @Damage[6d6[fire]|options:area-damage] damage (DC 21 [[Reflex]] save). Creatures that fail the save also fall [[Prone]] as they slip in the greasy blood. <br>  <br> The brimorak can't use Frothing Spew again for 1d4 rounds."
  - name: "Fume"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The brimorak emits a cloud of thick black smoke in a @Template[burst|distance:10] adjacent to them. The cloud remains for 1 minute. All creatures within the smoke become [[Concealed]], and all creatures outside the smoke become concealed to creatures within it. <br>  <br> A creature that enters or begins its turn within the smoke it must succeed at a DC 21 [[Fortitude]] save or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These goat-headed demons have glowing red eyes and flaming hooves. Born from the souls of arsonists, the fiery brimoraks continue the work they pursued in life, as everything they touch quickly burns.

Brimoraks are ill-tempered even for demons, although their spite turns to glee in the face of a growing fire. Those who have survived encounters with these fiends report that they remember the braying sound of the brimoraks' laughter as clearly as the heat of the flames or the choking scent of smoke.

When a sinful mortal soul is judged and sent on to the Outer Rifts, it can become a deadly fiend—a demon. Demons are living incarnations of sin—be they classic sins like wrath or gluttony, or more "specialized" depravities like an obsession with torture or the act of treason or treachery. Once formed, a demon's driving goals are twofold—the amassing of personal power, and the corruption of mortal souls to cause them to become tainted by sin. In this way demons ensure a never-ending supply of new demons to bolster their ever-growing ranks in the Outer Rifts.

Demons are selfish and self-absorbed creatures, and most firmly believe that mortals only play at being more virtuous than fiends. They enjoy tempting mortals into damnation to both indulge their egos and swell their armies. Like many other fiends, one of the great rewards of this manipulation is fulfilling their hunger for souls. In their eyes, the primary use for these souls is to spawn new demons, who can serve as soldiers, slaves, pawns, or even currency for their more powerful masters.

```statblock
creature: "Brimorak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
