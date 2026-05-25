---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Loan Shark"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +9, Deception +8, Diplomacy +8, Intimidation +8, Society +15, Accounting Lore +17"
abilityMods: ["+3", "+0", "+1", "+2", "+2", "+4"]
abilities_top:
  - name: "Business Savvy"
    desc: "When making monetary deals, the loan shark gets a +8 circumstance bonus to Deception checks, Diplomacy checks, and their Perception DC."
  - name: "Loan Specialist"
    desc: "For encounters involving monetary deals, the loan shark is a 7th-level challenge."
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "25"
abilities_mid:
  - name: "Never off the Hook"
    desc: "60 feet. <br>  <br> Creatures in the aura who owe the loan shark money take a –3 circumstance penalty to their Will DC against the loan shark's attempts to `act demoralize` or `act coerce` them and can't reduce their [[Frightened]] value below 1 while in the aura. <br>  <br> > [!danger] Effect: Owe Money"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dragon-Headed Cane +10 (`pf2:1`) (two hand d8), **Damage** 1d4+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Interest is Due!"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The loan shark commands an ally within 30 feet to attack a creature who owes the loan shark money. The ally can use a reaction to Strike the debtor, dealing an additional 1d6 mental damage. <br>  <br> > [!danger] Effect: Interest is Due!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Loan sharks lend money to those in need but charge high interest. If there's ever an issue with repayment, they'll send their gang to ensure clients pay in full.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Loan Shark"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
