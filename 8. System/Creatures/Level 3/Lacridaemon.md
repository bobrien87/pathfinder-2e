---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lacridaemon"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Daemonic (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Deception +9, Stealth +9, Survival +8"
abilityMods: ["+1", "+4", "+2", "+0", "+1", "+2"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Lacridaemon Venom"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 3** 1d8 poison damage, [[Confused]], and stupefied 1 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +12, **Will** +6"
health:
  - name: HP
    desc: "45; **Immunities** cold, death effects; **Weaknesses** holy 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Steal Bearings"
    desc: "`pf2:r` **Trigger** A creature within 30 feet Strides <br>  <br> **Effect** The lacridaemon attempts to redirect the triggering creature so it eventually becomes as lost as the lacridaemon. The triggering creature attempts a DC 17 [[Will]] save. Regardless of the result, the creature becomes temporarily immune to all attempts to Steal Bearings for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature treats all squares as difficult terrain for its Stride. <br> - **Critical Failure** As failure, except that the lacridaemon determines where the target moves during the Stride, though it can't move it into hazardous terrain or a place it can't stand."
  - name: "Weeping Aura"
    desc: "60 feet. The sounds of crying constantly surround a lacridaemon. A creature that first enters the area must attempt a DC 17 [[Will]] save as the sounds cause major disorientation. On a failure, the creature takes a –2 status penalty to Survival checks to Sense Direction (–4 on a critical failure) for 1 day. After attempting the save, the creature is temporarily immune to the lacridaemon's weeping aura for 1 day. The penalties from multiple weeping auras can increase up to a cumulative total of –10. <br>  <br> > [!danger] Effect: Weeping Aura"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (magical, unholy), **Damage** 1d8+4 piercing plus 1d6 cold plus [[Lacridaemon Venom]]"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, magical, unholy), **Damage** 1d6+4 slashing plus 1d6 cold"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +0<br>**2nd** [[Invisibility]]<br>**1st** [[Fear]], [[Vanishing Tracks]]"
abilities_bot:
  - name: "Venomous Spray"
    desc: "`pf2:2` The lacridaemon's begins to weep, spraying its venom-filled tears at all creatures within @Template[emanation|distance:30]{30 feet}. The creatures are immediately exposed to lacridaemon venom. Other lacridaemons are immune to this venom."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Souls who die from neglect or exposure due to becoming lost, trapped in small spaces, or otherwise being far from help can transform into lacridaemons. These weaker daemons are full of despair and typically lash out against anyone they see, believing them to have intentionally abandoned the lacridaemon to their fate. Many lacridaemons are born from the souls of wicked mortals who push others away and thus suffer lonely deaths. Exiled, corrupt nobles and violent criminals left to rot in solitary prisons are common among their ranks.

Lacridaemons tend to resemble humanoids with smooth, gray skin, a strange tail, and vicious claws. They each have patches of frost across their flesh, representing their ultimately cold and lonely ends. These patches appear on every lacridaemon even if their deaths weren't due to exposure to cold, as is the case for souls who perished alone from thirst in the desert.

Even in their fiendish state, lacridaemons can't help but consider themselves alone. It's not uncommon to find groups of lacridaemons where each daemon acts independently, as if the others weren't there. They tend to sit alone in dark corners reminiscent of the places of they died, sobbing loudly, but once they become aware of the presence of non-fiends, they are quick to attack, believing these creatures to be the same ones who abandoned them in life. A lacridaemon's supernatural abilities allow the fiend to subject others to a fate similar to the their own death, making it difficult to escape danger and find help.

```statblock
creature: "Lacridaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
