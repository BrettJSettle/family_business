
class MobFamily:

  def __init__(self, name: str, members: list[str]):
    self.name = name
    self.members = members  # List to store 9 mob member cards

MOB_FAMILIES = {
    family.name: family
    for family in [
        MobFamily(
            "Bank Robbers",
            [
                "ALVIN KARPIS",
                "BABY FACE NELSON",
                'KATE "MA" BARKER',
                'CHARLES "PRETTY BOY" FLOYD',
                'JOHN "DESPERATE DAN" DILLINGER',
                'GEORGE "MACHINE GUN" KELLY',
                'ARTHUR "DOC" BARKER',
                "BONNIE PARKER",
                "CLYDE BARROW",
            ],
        ),
        MobFamily(
            "Capone Mob",
            [
                'ALPHONSE "SCARFACE AL" CAPONE',
                'ANTHONY "BIG TUNA" ACCARDO',
                'WILLIAM JACK "THREE-FINGERED JACK" WHITE',
                'FRANK "THE ENFORCER" NITTI',
                'JACK "MACHINE GUN JACK" MCGUMN',
                'JACOU "GREASY THUMB" GUZIK',
                'SAM "THE GORILLA" DAVIS',
                'SAM "GOLFBAG" HUNT',
                'PAUL "THE WAITER" RICCA',
            ],
        ),
        MobFamily(
            "Murder, Inc.",
            [
                'IRVING "KILLER" NITZBERG',
                'HARRY "PITTSBURGH PHIL" STRAUSS',
                'ABRAHAM "KID TWIST" RELES',
                'ABRAHAM "PRETTY" LEVINE',
                'MARTIN "BUGSY" GOLDSTEIN',
                'ANTHONY "THE DUKE" MAFFETONE',
                'HARRY "HAPPY" MAIONE',
                'FRANK "THE DASHER" ABBENDADO',
                'ALBERT "TICK TOCK" TANNENBAUM',
            ],
        ),
        MobFamily(
            "Moran Gang",
            [
                "HYMIE WEISS",
                "WILLIE MANKS",
                "PETE GUSENBERG",
                'GEORGE "BUGS" MORAN',
                "AL WEINSHANK",
                "JAMES CLARK",
                "ADAM HEYER",
                "FRANK GUSENBERG",
                "JOEN MAY",
            ],
        ),
        MobFamily(
            "Purple Gang",
            [
                "JOSEPH BERNSTEIN",
                'SAMUEL "SAMMY PURPLE" COMEN',
                "PETER LICAVOLI",
                "EDDIE FLETCHER",
                "LOUIS FLEISHER",
                "JOSEPH ZERILLI",
                "HARRY FLEISHER",
                "ABE AXELROD",
                "BENJAMIN BERNSTEIN",
            ],
        ),
        MobFamily(
            "New York Gang",
            [
                "JOE VALACHI",
                "MEYER LANSKY",
                'CHARLES "LUCKY" LUCIANO',
                "DUTCH SHULTZ",
                'JOSEPH "JOE BANANAS" BONANNO',
                "VITO GENOVESE",
                "FRANK CORTELLO",
                'BENJAMIN "BUGSY" SIEGEL',
                'ALBERT "THE EXECUTIONER" ANASTASIA',
            ],
        ),
    ]
}