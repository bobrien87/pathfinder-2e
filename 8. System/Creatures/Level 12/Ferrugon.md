---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ferrugon"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Greater Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean, Talican (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +25, Crafting +22, Deception +21, Intimidation +23, Religion +22, Stealth +23, Thievery +25"
abilityMods: ["+7", "+5", "+6", "+4", "+4", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Ferrugon Tetanus"
    desc: "**Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Onset** 1d4 days <br>  <br> **Stage 1** [[Clumsy]] 1 (1 week) <br>  <br> **Stage 2** [[Clumsy]] 2 and can't speak (1 day) <br>  <br> **Stage 3** [[Paralyzed]] (1 day) <br>  <br> **Stage 4** death"
  - name: "Sunder Objects"
    desc: "When a ferrugon damages an item or structure, they deal an additional 2d8 damage to that item or structure."
armorclass:
  - name: AC
    desc: "33; **Fort** +24, **Ref** +20, **Will** +21"
health:
  - name: HP
    desc: "190; **Immunities** fire; **Weaknesses** holy 10; **Resistances** physical 10 except silver"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Metallic"
    desc: "A ferrugon is a metallic creature and thus affected by effects such as the circumstance penalty inflicted by [[Thunderstrike]]."
  - name: "Vainglorious Whispers"
    desc: "`pf2:r` **Trigger** A non-devil creature within 30 feet of the ferrugon succeeds (but doesn't critically succeed) at an attack roll, skill check, or saving throw <br>  <br> **Effect** The ferrugon whispers subversive messages to the triggering creature, causing it to become overly confident in its abilities, while in fact it becomes less accomplished overall. The target must attempt a DC 32 [[Will]] save. On a failure, the target gains a +2 status bonus to saving throws against fear effects but also takes a –2 penalty to all attack rolls and skill checks for 1 hour. During this time, the victim can't benefit from [[Aid]] reactions, use healing effects on themselves, or use [[Take Cover]] or Raise a Shield actions, as these actions seem unnecessary to the creature at this time. Similar defensive actions might not be available to the victim as well, at the GM's discretion. The target is then temporarily immune to Vainglorious Whispers for 24 hours. <br>  <br> > [!danger] Effect: Vainglorious Whispers"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +25 (`pf2:1`) (cold iron, magical, shove, unarmed, unholy), **Damage** 3d8+16 bludgeoning"
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (agile, cold iron, magical, unarmed, unholy), **Damage** 3d4+16 slashing plus [[Ferrugon Tetanus]]"
  - name: "Ranged strike"
    desc: "Iron Feather +23 (`pf2:1`) (cold iron, magical, unholy, range 40 ft.), **Damage** 3d4 + 13 piercing plus [[Ferrugon Tetanus]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24<br>**6th** [[Petrify (target is transformed into rusty iron, not stone)]]<br>**5th** [[Wall of Stone (wall is made of rusty iron, not stone)]]<br>**4th** [[Creation]], [[Suggestion]], [[Translocate]], [[Translocate]] (At Will)<br>**2nd** [[Shatter]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These ram-headed devils have wings and flesh made of rusted metal. They're forged from the souls of damned mortals who made others suffer through their creative work. They like to tempt those of the same ilk, driving auteurs and stage directors to cruelty in the pursuit of greatness. Ferrugons also enjoy pushing artists to extremes in order to break them. They dip the bodies of mortals they've driven to despair into molten metal to make horrifically malformed statues, which they then add to their lairs.

Rust devils prefer temptation to fighting and only enter combat if protecting something dear to them.

```statblock
creature: "Ferrugon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
