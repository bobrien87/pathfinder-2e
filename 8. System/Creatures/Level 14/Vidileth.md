---
type: creature
group: ["Aberration", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vidileth"
level: "14"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]]"
languages: "Aklo, Alghollthu, Common, Sakvroth, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +27, Athletics +24, Deception +28, Intimidation +26, Occultism +29, Society +27, Stealth +24, Lore (any one subcategory) +29"
abilityMods: ["+6", "+6", "+8", "+7", "+5", "+6"]
abilities_top:
  - name: "Numbing Lights"
    desc: "30 feet. <br>  <br> The vidileth exudes dim light. Creatures within the light must attempt a DC 34 [[Will]] save each round, becoming [[Stupefied 1]] on a failure (or increase their stupefied value from numbing lights by 1, to a maximum of 4)."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Consume Memories"
    desc: "When the vidileth hits with a fangs Strike, the target must succeed at a DC 34 [[Will]] save or take 3d6 mental damage. The vidileth gains temporary Hit Points equal to the damage dealt and learns some of the creature's memories (subject to the GM's discretion)."
  - name: "Delayed Suggestion"
    desc: "When a vidileth successfully casts [[Dominate]] on a creature, a [[Suggestion]] spell triggers when the *dominate* spell ends. This *suggestion* usually causes the target to return to the vidileth, so the creature can cast *dominate* again, but a vidileth can set the *suggestion* to different orders if it wishes."
  - name: "Thoughtlance"
    desc: "A creature touched by the vidileth's tentacles must attempt a DC 34 [[Will]] save, becoming [[Slowed]] 1 on a failure or [[Slowed]] 2 on a critical failure. Each time the affected creature ends its turn, its slowed value decreases by 1."
armorclass:
  - name: AC
    desc: "34; **Fort** +26, **Ref** +22, **Will** +24"
health:
  - name: HP
    desc: "270; **Immunities** controlled, electricity, mental; **Resistances** cold 20"
abilities_mid:
  - name: "+2 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +28 (`pf2:1`) (agile, magical, reach 20 ft., unarmed), **Damage** 3d10+12 slashing plus [[Shape Flesh]]"
  - name: "Melee strike"
    desc: "Fangs +28 (`pf2:1`) (magical, reach 10 ft., versatile s), **Damage** 3d8+12 piercing plus [[Consume Memories]]"
  - name: "Melee strike"
    desc: "Tentacle +28 (`pf2:1`) (agile, electricity, magical, reach 20 ft., unarmed), **Damage** 7d6 electricity plus [[Thoughtlance]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37, attack +29<br>**7th** [[Project Image]] (At Will)<br>**6th** [[Dominate]]<br>**5th** [[Illusory Scene]] (At Will), [[Sending]] (At Will), [[Truespeech]] (Constant)<br>**4th** [[Mirage]] (At Will), [[Suggestion]], [[Translocate]]<br>**3rd** [[Hypnotize]] (At Will), [[Levitate]] (At Will), [[Mind Reading]] (At Will)<br>**2nd** [[Water Breathing]] (At Will)<br>**1st** [[Illusory Disguise]] (At Will), [[Illusory Object]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Effect** A vidileth takes on the appearance of a humanoid of Large, Medium, or Small size or resumes its true form. While in humanoid form, the vidileth's Speed is 30 feet, and it loses its numbing lights aura and swim Speed. If the humanoid form assumed lacks the aquatic trait, the vidileth loses its own aquatic trait as well. In humanoid form, the vidileth can use weapons or make Strikes that work like its tentacle attack but use the reach of its current form. If the form has fangs or claws, the vidileth can also make such Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Shape Flesh"
    desc: "`pf2:1` **Requirements** The vidileth's last action was a success with a claw Strike <br>  <br> **Effect** The vidileth sloppily modifies the target's flesh. They must succeed at a DC 34 [[Fortitude]] save or permanently receive the veiled master's choice of [[Clumsy]] 2, [[Enfeebled]] 2, or a –10 status penalty to Speed."
  - name: "Tentacle Flurry"
    desc: "`pf2:2` The vidileth makes a tentacle Strike against each creature within its reach. Make only one attack roll, and roll damage once for all targets."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The powerful vidileths are the insidious veiled masters of the alghollthus. These manipulators of mind and body alike lead their species in the open, using their ability to change form to walk among and deceive humans and other sapient species. Many veiled masters are even more powerful than the typical specimen presented here and can use a wide range of arcane or occult spells and rituals. While veiled masters command significant combat prowess and impressive magical skills, the greatest danger they pose to others is their uncanny ability to infiltrate into societies much different than their own. The most paranoid of adventurers and conspiracy scholars worry that every major city has been infested by secret cabals of vidileths, while others dismiss this as hogwash and fearmongering. The truth is likely somewhere in between, but it doesn't take many veiled masters pulling the strings behind the scenes to wreak havoc upon an entire nation!

In bygone millennia, aquatic monsters known as alghollthus used their occult powers to conquer and rule vast parts of the world. Their empires contained countless mortal slaves treated as little more than cattle. Alghollthus shaped their slaves and other creatures using mental manipulation and physically transformative magic. Aberrant horrors from faceless stalkers to mimics can be traced back to this meddling. The rulers of the alghollthu race, the so-called veiled masters, further shaped entire societies by assuming the forms of those they controlled. From the heights of power to the shadows of poverty, the veiled masters manipulated these societies according to their own dark designs, enslaving, killing, or horrifically transforming those who discovered their plans or acted against them.

In time, the alghollthus grew frustrated with their increasingly upstart slave societies and sought to wipe the slate clean-both starting anew and punishing those who had become too willful and rebellious. They used incredible magical power to call forth a cataclysm, hoping to destroy the rebellious societies they'd manipulated. Yet they miscalculated the strength of faith and will to survive of their pawns and slaves, and in time the world and its empires recovered and grew strong once again-this time without alghollthu influence.

Today, the alghollthus have retreated from their mass-scale manipulation of the surface world, and they have mostly remained within the deep aquatic realms where they still rule without question. Yet they have not abandoned their plots entirely, and the reemergence of servitor races like ugothols points to a frightening possibility-that the alghollthus have turned their hateful eyes to the surface once again.

```statblock
creature: "Vidileth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
