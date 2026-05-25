---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lich"
level: "12"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Elven, Necril, Sakvroth"
skills:
  - name: Skills
    desc: "Arcana +28, Crafting +24, Deception +17, Diplomacy +19, Religion +22, Stealth +20"
abilityMods: ["+0", "+4", "+0", "+6", "+4", "+3"]
abilities_top:
  - name: "Siphon Life"
    desc: "A lich's form draws forth life from those who come into contact with it. When the lich damages a living creature with an unarmed attack, the lich gains 5 temporary Hit Points and the creature must succeed at a DC 34 [[Fortitude]] save or become [[Drained]] 1. <br>  <br> If the lich is [[Grabbed]] or [[Restrained]] at the start of its turn, each creature grabbing or restraining it must succeed at a Fortitude save or become drained 1. If the lich siphons a creature's life again, the drained value increase by 1, to a maximum of [[Drained]] 4."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted."
armorclass:
  - name: AC
    desc: "31; **Fort** +17, **Ref** +21, **Will** +23"
health:
  - name: HP
    desc: "190; void healing, rejuvenation; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Vitality"
    desc: ""
  - name: "Counterspell"
    desc: "`pf2:r` **Trigger** A creature casts a spell the lich has prepared. <br>  <br> **Effect** The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses its spell slot as if it had cast the triggering spell. The lich then attempts to counteract the triggering spell."
  - name: "Frightful Presence"
    desc: "60 feet. DC 29 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Rejuvenation"
    desc: "When a lich is destroyed, its soul immediately transfers to their *[[Lich Soul Cage]]*. A lich can be permanently destroyed only if their *soul cage* is found and destroyed."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hand +24 (`pf2:1`) (finesse, magical), **Damage** 4d8 void plus [[Siphon Life]]"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26<br>**6th** (3 slots) [[Chain Lightning]], [[Dominate]], [[Vampiric Exsanguination]]<br>**5th** (4 slots) [[Howling Blizzard]], [[Howling Blizzard]], [[Toxic Cloud]], [[Wall of Ice]]<br>**4th** (4 slots) [[Dispel Magic]], [[Fire Shield]], [[Fly]], [[Translocate]]<br>**3rd** (4 slots) [[Blindness]], [[Force Barrage]], [[Locate]], [[Vampiric Feast]]<br>**2nd** (4 slots) [[Blur]], [[False Vitality]], [[Resist Energy]], [[See the Unseen]]<br>**1st** (4 slots) [[Enfeeble]], [[Enfeeble]], [[Fleet Step]], [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Message]], [[Shield]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Drain Soul Cage"
    desc: "`pf2:0` 6th rank <br>  <br> **Frequency** once per day <br>  <br> **Effect** The lich taps into their *[[Soul Cage]]*'s power to cast any arcane spell up to the highest rank the lich can cast, even if the spell being cast is not one of the lich's prepared spells. The lich's soul cage doesn't need to be present for the lich to use this ability."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A wizard whose insatiable desire for arcane power eclipsed their mortal life, the lich is a truly devious and versatile spellcaster.

To gain more time to complete their goals, some desperate spellcasters pursue immortality by embracing undeath. After long years of research and the creation of a special container called a phylactery, a spellcaster takes the final step by imbibing a deadly concoction or casting dreadful incantations that transform them into a lich. While most undertake this drastic plan to continue their work or fulfill some long-term plan, others become liches because they fear death or to fulfill some malevolent purpose, such as long-sworn revenge. Regardless, the result is permanent and carries with it the potential to alter history-both that of those who transform themselves and of the countless mortals that will inevitably suffer as a result of a lich's new power.

After its metamorphosis, a lich often finds some quiet place to dwell, typically protected by a variety of guardians and traps, for two primary purposes. First, a lich requires solitude in order to plan its elaborate schemes, and second, few mortals (if any) deign to interact with these legendarily corrupt necromancers. One reason begets the other, as the self-imposed isolation of a lich often drives the lich insane, further solidifying its separation from civilization. The longer a lich lives, the more meticulous a planner it becomes, secreting itself within a labyrinth of deadly puzzles, misdirection, and monsters. A lich's servants and guardians are absolutely loyal, either due to their nature (such as constructs or other undead) or as a result of compulsion using powerful magic. Many liches go mad, in time, and the nature of a lich's lair is a good indicator of the undead's current mental state.

For all the protections it arrays around itself, a lich will go to greater lengths to guard its phylactery, as it knows that the destruction of this magical container spells doom for the lich. A lich is notoriously difficult to bargain with, though the threat of damaging its phylactery is a sure way to gain the upper hand in such a negotiation.

```statblock
creature: "Lich"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
